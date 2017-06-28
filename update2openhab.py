#!/usr/bin/env python
from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY
import requests
import json
import datetime

openhab_host = 'openhabianpi'
openhab_port = '8080'
#defekt 'C4:7C:8D:62:E6:A8'
mac_addresses = ['C4:7C:8D:62:E6:B7','C4:7C:8D:63:64:44','C4:7C:8D:63:74:E8','C4:7C:8D:63:35:BA','C4:7C:8D:63:7B:BF',]
flower_names = ['Lavendel','Olivenbaum','TomTato','Sommermargerite','Maennertreu']

def send_status_to_openhab(flower, key, value):
    url = 'http://{host}:{port}/rest/items/MiFlora_{flower}_{key}/state'.format(host=openhab_host, port=openhab_port, flower=flower, key=key)

    if value == None:
        value = ""

    try:
        response = requests.put(url, headers={'Content-Type': 'text/plain'}, data=json.dumps(value))
        print(datetime.datetime.now(), 'updated', url,'=', value)
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
    except Exception as e:
            print(datetime.datetime.now(), "-Error-")
            print(datetime.datetime.now(), 'updating', key , "=", value)
            print(datetime.datetime.now(), e)

for index in range(len(mac_addresses)):
    try:
        poller = MiFloraPoller(mac_addresses[index])
        print(datetime.datetime.now(), "Getting data from Mi Flora '" , flower_names[index],"'" )
        send_status_to_openhab(flower=flower_names[index],key='Firmware', value=poller.firmware_version())
        send_status_to_openhab(flower=flower_names[index],key='Temperature', value=poller.parameter_value("temperature"))
        send_status_to_openhab(flower=flower_names[index],key='Moisture', value=poller.parameter_value(MI_MOISTURE))
        send_status_to_openhab(flower=flower_names[index],key='Light', value=poller.parameter_value(MI_LIGHT))
        send_status_to_openhab(flower=flower_names[index],key='Conductivity', value=poller.parameter_value(MI_CONDUCTIVITY))
        send_status_to_openhab(flower=flower_names[index],key='Battery', value=poller.parameter_value(MI_BATTERY))
        print(datetime.datetime.now(), "Finished!")
    except Exception as e:
        print(datetime.datetime.now(), "-Error-")
        print(datetime.datetime.now(), e)
