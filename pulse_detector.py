import utime, ujson
from machine import Pin, UART

slowCounter = 0
fastCounter = 0
time_t0 = utime.ticks_ms()
msgArr = []


def inc_slow_counter(Pin):    
    global slowCounter, fastCounter, time_t0, uart1, msgArr, ws
    slowCounter += 1
    time_diff_ms = utime.ticks_diff(utime.ticks_ms(), time_t0)    
    time_t0 = utime.ticks_ms()  #update time_t0 with new time
    uartStr = "Rotation # " + str(slowCounter) + " -- Contado # " + str(fastCounter)
    uartStr += " -- Tiempo : " + str(time_diff_ms) + " ms "  + "\n"
    print(uartStr)
    #uart1.write( bytearray(uartStr) )    
    uart1.write( uartStr )    
    
    msgJson = {}
    msgJson['slowCounter'] = slowCounter
    msgJson['fastCounter'] = fastCounter
    msgJson['timeDiff'] = str(time_diff_ms)
    msgJson['timeDiff_units'] = "ms"
    msgJson['timeT0'] = str(time_t0)

    msgArr.append(msgJson)

    try:
        if ws.webSocketItem._mws2.IsRunning :
            # ws.webSocketItem.SendTextMessage(uartStr)
            
            ws.webSocketItem.SendTextMessage( ujson.dumps(msgJson) )
    except:#NameError: #AttributeError:
        pass

    fastCounter = 0

    #eg1 = bytearray()
    #eg1.append(0x30)
    #test22= str('6', 'UTF-8')
    #uart1.write( bytearray('6' , 'ASCII') )
    #report_slow_counters_to_lcd(slowCounter, fastCounter)
    
    #report_fast_counters_to_lcd(slowCounter, fastCounter)
    

def inc_fast_counter(GPIO):    
    global slowCounter, fastCounter    
    fastCounter += 1
    #print("fast count: ", fastCounter, "\n")
    #report_fast_counters_to_lcd(slowCounter, fastCounter)


uart1 = UART(2, 9600)
uart1.init(9600,bits=8,parity=None,stop=1)
#                    ,timeout=1000, buf_size=1024, lineend=b'\r\n' , read_buf_len=4096 )


#Instantiate GPIO and define properties of PINs
slowCountPin=Pin( 18 , Pin.IN, Pin.PULL_DOWN)
fastCountPin=Pin( 19 , Pin.IN, Pin.PULL_DOWN)

#leave a tiny delay ... why, I don't know... so for magic reasons...
utime.sleep_ms(500)


#read pin values into memory, then define Interrupt function requests
slowCountPin.value()
slowCountPin.irq(handler=inc_slow_counter,trigger=Pin.IRQ_RISING )# , priority=7, wake=None, hard=False )

fastCountPin.value()
fastCountPin.irq(handler=inc_fast_counter,trigger=Pin.IRQ_RISING )#,GPIO.WAKEUP_NOT_SUPPORT,7)

import wlan_ap_init

utime.sleep(1)

import ws_server as ws

wserv2 = ws.WS_Server()

#report_slow_counters_to_lcd(0, 0)
#report_fast_counters_to_lcd(0, 0)
#key.disirq()
#fm.unregister(board_info.BOOT_KEY,fm.fpioa.GPIOHS0)

#while (True):
#    uart1.write(bytearray( b'A', 'ASCII') )
