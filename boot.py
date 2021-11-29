# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
webrepl.start()
import pulse_detector
#import wlan_sta_init   #Connect to local wifi, and listens on static IP address
import wlan_ap_init		#Creates an AccessPoint, letting user connect directly to webserver