from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import context
# from pysnmp.entity.rfc3413.asyncio import ntforg
from pysnmp.entity.rfc3413.asyncio import ntforg
from pysnmp.carrier.asyncio.dgram import udp
from pysnmp.proto import rfc1902
import trollius

# Get the event loop for this thread
loop = trollius.get_event_loop()

# Create SNMP engine instance
snmpEngine = engine.SnmpEngine()

# SNMPv1 setup

# SecurityName <-> CommunityName mapping
config.addV1System(snmpEngine, 'my-area', 'public')

# Specify security settings per SecurityName (SNMPv1 -> 0)
config.addTargetParams(snmpEngine, 'my-creds', 'my-area', 'noAuthNoPriv', 0)

# Transport setup
#
# Setup transport endpoint and bind it with security settings yielding
# a target name. Since Notifications could be sent to multiple Managers
# at once, more than one target entry may be configured (and tagged).
#

# UDP/IPv4
config.addTransport(
    snmpEngine,
    udp.domainName,
    udp.UdpTransport().openClientMode()
)
config.addTargetAddr(
    snmpEngine, 'my-nms-1',
    udp.domainName, ('127.0.0.1', 162),
    'my-creds',
    tagList='all-my-managers'
)

# Specify what kind of notification should be sent (TRAP or INFORM),
# to what targets (chosen by tag) and what filter should apply to
# the set of targets (selected by tag)
config.addNotificationTarget(
    snmpEngine, 'my-notification', 'my-filter', 'all-my-managers', 'trap'
)

# Allow NOTIFY access to Agent's MIB by this SNMP model (1), securityLevel
# and SecurityName
config.addContext(snmpEngine, '')
config.addVacmUser(snmpEngine, 1, 'my-area', 'noAuthNoPriv', (), (), (1,3,6))

@trollius.coroutine
def snmpOperation(snmpEngine, target, snmpContext, contextName,
                  notificationName, instanceIndex, additionalVarBinds):
    future = ntforg.NotificationOriginator().sendVarBinds(
        snmpEngine,
        target,
        snmpContext,
        contextName,
        notificationName,
        instanceIndex,
        additionalVarBinds
    )

    # We know we are sending TRAP which will never produce any response.
    # Therefore we simulate successful response here.
    future.set_result((snmpEngine, None, 0, 0, ()))

    ( snmpEngine,
      errorIndication,
      errorStatus,
      errorIndex, 
      varBinds ) = yield trollius.From(future)
 
    if errorIndication:
        print(errorIndication)

    # This also terminates internal timer
    config.delTransport(
        snmpEngine,
        udp.domainName
    )

# Initiate sending SNMP message
trollius.async(
    snmpOperation(
        snmpEngine,
        # Notification targets
        'my-notification',
        # Default SNMP context where contextEngineId == SnmpEngineId
        context.SnmpContext(snmpEngine),
        # contextName
        '',
        # notification name: Generic Trap #6 (enterpriseSpecific)
        #                    and Specific Trap 432
        '1.3.6.1.4.1.20408.4.1.1.2.0.432',
        # notification objects instance index
        None,
        # additional var-binds holding SNMPv1 TRAP details
        [
            # Uptime value with 12345
            (rfc1902.ObjectName('1.3.6.1.2.1.1.3.0'),
             rfc1902.TimeTicks(12345)),
            # Agent Address with '127.0.0.1'
            (rfc1902.ObjectName('1.3.6.1.6.3.18.1.3.0'),
             rfc1902.IpAddress('127.0.0.1')),
            # Enterprise OID with 1.3.6.1.4.1.20408.4.1.1.2
            (rfc1902.ObjectName('1.3.6.1.6.3.1.1.4.3.0'),
             rfc1902.ObjectName('1.3.6.1.4.1.20408.4.1.1.2')),
            # managed object '1.3.6.1.2.1.1.1.0' = 'my system'
            (rfc1902.ObjectName('1.3.6.1.2.1.1.1.0'),
             rfc1902.OctetString('my system'))
        ]
    )
)

# Since SNMP TRAP's are unacknowledged, there's nothing to wait for. So we
# simulate other loop activities by sleep()'ing.
loop.run_until_complete(trollius.sleep(1))

# Clear the event loop
loop.close()
