# Imports
import socketio;
import time;

# Variables
sio = None;
exit_app = False;

# Functions
def connectToServer():

    try:
        sio.connect('https://netencrypt.devkrxspl.repl.co/:3000');
    except:
        while not exit_app:
            try:
                sio.connect('https://netencrypt.devkrxspl.repl.co/:3000');
            except:
                time.sleep(1);

def createClient():
    global sio;

    if (sio):
        return sio;

    sio = socketio.Client();

    return sio;

def disconnect():
    global exit_app;
    exit_app = True;

    if (sio and sio.connected):
        sio.disconnect();