# ESP32-IoT-button-graph-test
ESP32 recording button presses, and serving webpage via webSockets in order to graph the responses.
The objective was to test the ESP32 webSocket implementation written in microPython.

> To implement, upload `firmware.bin` to ESP32-dev board

> copy all `*.py` files and `*.html/js` to ESP32 root directory.

> connect two buttons, each with pull up resistors (1 KOhm), on pins 18 and 19 

> Pin 19 keeps track of `fastCountPin`, i.o.w.  high freq pulses.

> Pin 18 keeps track of `slowCountPin`, i.o.w.  low freq pulses (acts like a reset button to Pin 19 counter).

---


Used : WebSocket libs [ jczic / MicroWebSrv2 ](https://github.com/jczic/MicroWebSrv2/) 
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



The following snippet creates a webSocket instance.  The downside, is that the connection disconnects, but doesn't reconnect, if no activity detected. 

```
        function startingWS ()
        {
            ws = new WebSocket("ws://" + window.location.hostname);

            ws.onopen = function(evt) { 
              console.log("Connection open ..."); 
              ws.send("Hello WebSockets!");
            };

            ws.onmessage = function(evt) {
              console.log( "Received Message: " + evt.data);
              msgJson = JSON.parse(evt.data);
              if(msgJson.slowCounter > counter)
              {
                console.log(msgJson.timeDiff);
              }
              pulses_dataValuesArr.push(msgJson.fastCounter);
              pulses_datalabelStructure.push(counter);

              timing_dataValuesArr.push(msgJson.timeDiff);
              timing_datalabelStructure.push(counter);

            chartPulses.update();
            chartTiming.update();

              counter += 1;
              //
            };

            ws.onclose = function(evt) {
              console.log("Connection closed.");
            };

            ws.closeConn = () => {
                ws.close();
            }
        }
```


