# Imports
from sys import stdout
import threading

from npyscreen.compatibility_code.oldtreeclasses import MultiLineTreeNewAction
from util import terminal;

import npyscreen;
import socketio;
import time;
import curses;

# Classes
class App(npyscreen.NPSAppManaged):

    def onStart(self):

        global sio;
        global connected;

        # App Main
        sio = socketio.Client();
        self.registerForm("MAIN", MainMenu());
        npyscreen.disableColor(); # Bad support for color, just disable
        terminal.init();

        # Socket Main
        def connectToServer():
            try:
                sio.connect('https://netencrypt.devkrxspl.repl.co/:3000');
            except:
                while True:
                    try:
                        sio.connect('https://netencrypt.devkrxspl.repl.co/:3000');
                    except:
                        time.sleep(1);

            # Connection established
        
        threading.Thread(target=connectToServer).start();
                

class MainMenu(npyscreen.FormBaseNew):
    def create(self):

        # Creating form
        y_max, x_max = curses.initscr().getmaxyx();

        menu_title = "Welcome to NetEncrypt";
        menu_button_length = 10;

        self.add(npyscreen.TitleFixedText, name = menu_title, relx = (x_max - 23) // 2, rely = y_max // 2 - 5);
        self.add(npyscreen.ButtonPress, name="[ Login ]", relx = (x_max - 14) // 2, rely = y_max // 2 - 3, when_pressed_function=self.login);
        self.add(npyscreen.ButtonPress, name="[ Exit  ]", relx = (x_max - 14) // 2, rely = y_max // 2 - 1, when_pressed_function=self.exit);
        connection_status = self.add(npyscreen.FixedText, name="Disconnected", relx=2, rely=1);

        # Connected
        @sio.event 
        def connect():
            connection_status.value = "Connected";
            connection_status.display();

        # Disconnected
        @sio.event 
        def disconnect():
            connection_status.value = "Disconnected";
            connection_status.display();

    def login(self):
        if (not sio.connected):

            npyscreen.notify_confirm("  Failed to establish a connection to the server.", "", form_color="WHITE_BLACK", editw=1);

            # ignore this im so stupid
            # self.parentApp.registerForm("MAIN", MainMenu());
            # self.parentApp.switchForm("MAIN");

    def exit(self):

        self.parentApp.switchForm(None);
            
        if (sio.connected):
            sio.disconnect();

        terminal.exit();


# Main
app = App();
app.run();