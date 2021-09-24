# Imports
import socketio;
import time;

# Variables
sio = None;

# Functions
def connectToServer():

    try:
        sio.connect('https://netencrypt.devkrxspl.repl.co/:3000');
    except:
        while True:
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