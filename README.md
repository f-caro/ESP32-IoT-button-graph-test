# ESP32-IoT-button-graph-test
ESP32 recording button presses, and serving webpage that graphs the numbers over time.


### Firmware was compiled from scratch in order to accomodate Websocket MicroPython Server files into 4MB flash memory.

Need to find the website that showed me howto compile ESP32 firmware in Linux Mint  (Was not an easy task.  Lots of trial and error).
```
boot.py :	
```
> starts the show 
> Need to enable which Wifi script to run ---  AccessPoint or local Wifi network
> Next enable the pulse_detector.py script,  which starts the button press detection


```
pulse_detector.py
```
> initiates PIN properties, init's webSocket server, increases pin counter, prepares JSON packet and transmits client endpoint  
> also outputs to terminal:  access via `screen /dev/ttyUSB0 115200`
>  JSON Packet
> `msgJson = {}`
> `msgJson['slowCounter'] = slowCounter`
> `msgJson['fastCounter'] = fastCounter`
> `msgJson['timeDiff'] = str(time_diff_ms)`
> `msgJson['timeDiff_units'] = "ms"`
> `msgJson['timeT0'] = str(time_t0) ` 
> `msgArr.append(msgJson)`

```
ws_server.py
```
> serves HTML / CSS and javascript files
> creates `/` server endpoints for each js,html, css file 

```
ws_index.html
```
> call JS scripts :  moment.min.js ( datetime libs ); Chart.min.js ( Chart libs in HTML5 <canvas> )  
>

#TODO : Need to further elaborate on the task at hand.