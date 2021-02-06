import os, json, machine, time
from umqtt.simple import MQTTClient
from machine import Pin, PWM


def save_file_and_restart(filename, content, restart=True):
    with open(filename, 'w') as f:
        f.write(content)
    if restart:
        client.disconnect()
        machine.reset()


heat = Pin(14, Pin.OUT)
cold = Pin(12, Pin.OUT)
device_id = 1


def sub_cb(topic, msg):
    print(topic)

    if topic == b'cup/1':
        jmsg = json.loads(msg.decode())
        if jmsg["command"] == 'on':
            if jmsg["mode"] == 'heat':
                cold.off()
                heat.on()
                client.publish('cup/1/answer', 'Heating')
            elif jmsg["mode"] == 'cold':
                heat.off()
                cold.on()
                client.publish('cup/1/answer', 'Colding')
        elif jmsg["command"] == 'off':
            heat.off()
            cold.off()
            client.publish('cup/1/answer', 'Off')

        else:
            client.publish('cup/1/answer', 'error')

    elif topic == b'cup/file':
        jmsg = json.loads(msg.decode())
        print(jmsg['filename'])
        filename = jmsg['filename']
        save_file_and_restart(filename, jmsg['file'])


with open('config.json', 'r') as x:
    cfg = json.load(x)
client = MQTTClient(cfg['client_id'], cfg['host'], 1883)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="cup/#")
while True:
    client.check_msg()
