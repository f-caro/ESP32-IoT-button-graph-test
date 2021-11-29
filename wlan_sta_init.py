import network
import time

station = network.WLAN(network.STA_IF)

essid_name='Anne marie'
essid_password='hn76773946'
#essid_name='PROMEL'
#essid_password='852aPRML'

station.active(True)

station.ifconfig(('192.168.1.130','255.255.255.0','192.168.1.1','8.8.8.8'))

#station.config(essid=essid_name, authmode=network.AUTH_WPA2_PSK , password=essid_password )
#station.config(authmode=network.AUTH_WPA2_PSK)


if not station.isconnected():
	#station.connect('Anne marie', 'hn76773946')
	station.connect('PROMEL', '852aPRML')
	print("Waiting for connection...")
	while not station.isconnected():
		time.sleep(1)
print(station.ifconfig())


print('ESP32 connected to :')

time.sleep(1)
station.ifconfig()
# while station.isconnected() == False:
#     pass

# print('Connection successful')
# print(station.ifconfig())

#led = Pin(2, Pin.OUT)
