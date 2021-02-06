import gc, network, json, os, machine

lst = os.listdir()
with open('config.json', 'r') as x:
    cfg = json.load(x)

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect(cfg['ssid'], cfg['pass'])
    while not sta_if.isconnected():
        pass
# newboot
gc.collect()