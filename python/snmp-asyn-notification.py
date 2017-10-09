from pysnmp.entity.rfc3413.oneliner import cmdgen, ntforg
from pysnmp.proto.api import v2c

def cbFun(sendRequestHandle, errorIndication, cbCtx):
    print 'sendRequestHandle =', sendRequestHandle
    print 'errorIndication =', errorIndication
    print 'cbCtx =', cbCtx

asynNotificationOriginator = ntforg.AsynNotificationOriginator()
# This is a non-blocking call
sendRequestHandle = asynNotificationOriginator.asyncSendNotification(
    cmdgen.UsmUserData('my-user', 'my-authkey', 'my-privkey'),
    cmdgen.UdpTransportTarget(('localhost', 162)), 'inform', 
    ('SNMPv2-MIB', 'coldStart'), ((1,3,6,1,2,1,1,1,0), 
    v2c.TimeTicks(44100)), (cbFun, None))
print sendRequestHandle

asynNotificationOriginator.snmpEngine.transportDispatcher.runDispatcher()
