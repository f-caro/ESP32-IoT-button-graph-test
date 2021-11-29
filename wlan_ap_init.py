import usocket as socket
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

station = network.WLAN(network.AP_IF)

station.active(True)
station.config(essid='ESP32_sensor1', authmode=network.AUTH_WPA2_PSK , password='12345678', channel=4)

print('ESP32_sensor1 AccessPoint started')
# while station.isconnected() == False:
#     pass

# print('Connection successful')
# print(station.ifconfig())

#led = Pin(2, Pin.OUT)
