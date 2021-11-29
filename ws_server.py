
from MicroWebSrv2  import *
from time          import sleep
from _thread       import allocate_lock
import uio


class WS_Server():
    #mws2
    #wsMod = ""
    #pyhtmlTemplateMod


    def __init__(self):
        # Loads the WebSockets module globally and configure it,
        global wsMod
        self.wsMod = MicroWebSrv2.LoadModule('WebSockets')

        self.wsMod._waitFrameTimeoutSec = 10000000

        self.wsMod.OnWebSocketAccepted = OnWebSocketAccepted

        self.pyhtmlTemplateMod = MicroWebSrv2.LoadModule('PyhtmlTemplate')
        self.pyhtmlTemplateMod.ShowDebug = True

        # Instanciates the MicroWebSrv2 class,
        self.mws2 = MicroWebSrv2()

        # SSL is not correctly supported on MicroPython.
        # But you can uncomment the following for standard Python.
        # mws2.EnableSSL( certFile = 'SSL-Cert/openhc2.crt',
        #                 keyFile  = 'SSL-Cert/openhc2.key' )

        # For embedded MicroPython, use a very light configuration,
        self.mws2.SetEmbeddedConfig()

        # All pages not found will be redirected to the home '/',
        self.mws2.NotFoundURL = '/'

        # Starts the server as easily as possible in managed mode,
        self.mws2.StartManaged()

    
    def loopMws2UntilKeyboardInterrupt(self):
        # Main program loop until keyboard interrupt,
        try :
            while self.mws2.IsRunning :
                sleep(1)
        except KeyboardInterrupt :
            pass

    def endMws2Instance(self):
        # End,
        print()
        self.mws2.Stop()
        print('Bye')
        print()

@WebRoute(GET, '/')
def RequestWsIndex(microWebSrv2, request) :
    # content = ""
    # f = uio.open('ws_index.html', mode='r')
    # for x in f:
    #     content += x
    #content = loadFile( 'ws_index.html' )
    #request.Response.ReturnOk(content)
    request.Response.ReturnFile('ws_index.html', attachmentName=None)

@WebRoute(GET, '/Chart.min.js')
def RequestWsIndex(microWebSrv2, request) :
    #content = loadFile( 'Chart.min.js' )
    #request.Response.ReturnOk(content)
    request.Response.ReturnFile( 'Chart.min.js' , attachmentName=None)

@WebRoute(GET, '/chartjs-plugin-streaming.min.js')
def RequestWsIndex(microWebSrv2, request) :
    request.Response.ReturnFile( 'chartjs-plugin-streaming.min.js' , attachmentName=None)

@WebRoute(GET, '/uikit.min.js')
def RequestWsIndex(microWebSrv2, request) :
    request.Response.ReturnFile( 'uikit.min.js' , attachmentName=None)

@WebRoute(GET, '/uikit.min.css')
def RequestWsIndex(microWebSrv2, request) :
    request.Response.ReturnFile( 'uikit.min.css' , attachmentName=None)

@WebRoute(GET, '/moment.min.js')
def RequestWsIndex(microWebSrv2, request) :
    request.Response.ReturnFile( 'moment.min.js' , attachmentName=None)



def loadFile( filename ):
    content = ""
    f = uio.open( filename, mode='r')
    for x in f:
        content += x
    f.close()
    return content

 # ============================================================================
def OnWebSocketAccepted(microWebSrv2, webSocket) :
    global webSocketItem
    print('Example WebSocket accepted:')
    print('   - User   : %s:%s' % webSocket.Request.UserAddress)
    print('   - Path   : %s'    % webSocket.Request.Path)
    print('   - Origin : %s'    % webSocket.Request.Origin)

    webSocketItem = webSocket
    
    # print(microWebSrv2.__module__)
    # print(microWebSrv2.__dict__)
    # print( dir(microWebSrv2) )
    # #print(help(microWebSrv2) )
    
    # print(webSocket.__module__)
    # print(webSocket.__dict__)
    # print( dir(webSocket) )
    # #print(help(webSocket) )

    webSocket.OnTextMessage   = OnWebSocketTextMsg
    webSocket.OnBinaryMessage = OnWebSocketBinaryMsg
    webSocket.OnClosed        = OnWebSocketClosed

# ============================================================================
def OnWebSocketTextMsg( webSocket, msg) :
    print('WebSocket text message: %s' % msg)
    webSocket.SendTextMessage('Received "%s"' % msg)
# ------------------------------------------------------------------------
def OnWebSocketBinaryMsg( webSocket, msg) :
    print('WebSocket binary message: %s' % msg)
# ------------------------------------------------------------------------
def OnWebSocketClosed( webSocket) :
    print('WebSocket %s:%s closed' % webSocket.Request.UserAddress)
# ============================================================================