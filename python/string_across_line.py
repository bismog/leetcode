#!/usr/bin/env python

ss = '''{
    "id": "sfa",
    "name": "power zone",
    "updateDate": "2014-09-11T01:15:16+08:00",
    "rackLocation": {
        "rackunits": 0,
        "xLocation": 0,
        "uLocation": 1,
        "uHeight": 8,
    },
    "presentPowerInput": 2700,
    "presentPowerOutput": 3200,
    "maxRatePowerCapacity": 5000,
    "maxPSUsSupported": 6,
    "numberOfPSUsPresent": 6
}'''

xx = '{ \
                "@odata.context": "/rest/v1/$metadata#RSADrawers/Links/Members/$entity", \
                "@odata.id": "/rest/v1/Drawers/1", \
                "@odata.type": "#RSADrawer.1.0.0.RSADrawer", \
                "Id": 1, \
                "Name": "RSA Drawer", \
                "Modified": "2015-03-20T14:44:00+00:00", \
                "ChassisType": "Shelf", \
                "Manufacturer": "Intel Corporation", \
                "Model": "BDC-A", \
                "SerialNumber": "", \
                "Status": { \
                "State": "Enabled",\
                "Health": "OK"\
                }, \
                "EnumStatus": "Enumerated"\
}'

print xx

