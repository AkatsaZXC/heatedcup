**HeatedCup**

_Software part:_

Idea of this project is pretty simple. We are using Peltier element
to heat or cold your cup with some liquid.

As transfer protocol used MQTT and Mosquitto broker.

In `config.json` you have to change field with `SSID`, `PASS` with your network configuration. 

And fields `HOST_IP` and `DEVICE_ID` for your MQTT broker.

_Hardware part_

As WiFi module we are using `NodeMCU ESP8266` module.
`Peltier element`, transistors `IRF3205` and `AC/DC Power Supply 5V 500mA`


