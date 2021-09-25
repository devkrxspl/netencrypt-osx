# Imports
import sys;
import npyscreen;
import curses;
import os;

# Leaving this subdirectory
sys.path.append("../netencrypt");

from util import terminal;
from util import notify;
from conn import client;

# Main
class MainMenu(npyscreen.FormBaseNew):

    def create(self):

        # Creating form
        y_max, x_max = curses.initscr().getmaxyx();

        menu_title = "Welcome to NetEncrypt";

        self.add(npyscreen.TitleFixedText, name = menu_title, relx = (x_max - 23) // 2, rely = 7);
        self.add(npyscreen.ButtonPress, name="[ Connect ]", relx = (x_max - 14) // 2, rely = 9, when_pressed_function=self.login);
        self.add(npyscreen.ButtonPress, name="[  Exit   ]", relx = (x_max - 14) // 2, rely = 11, when_pressed_function=self.exit);
        connection_status = self.add(npyscreen.FixedText, value="Disconnected", relx=2, rely=1);

        # Connected
        @client.sio.event 
        def connect():
            connection_status.value = "Connected - SID {}".format(client.sio.get_sid());
            connection_status.display();

        # Disconnected
        @client.sio.event 
        def disconnect():
            connection_status.value = "Disconnected";
            connection_status.display();

    def login(self):
        if (not client.sio.connected):
            y_max, x_max = curses.initscr().getmaxyx();
            notify.notify_confirm("  Failed to establish a connection to the server.", "", form_color="WHITE_BLACK", editw=1, width=x_max - 10, height=y_max//2, relx = 5, rely=3);

    def exit(self):

        self.parentApp.switchForm(None);
        
        terminal.exit();
        client.disconnect();
        os._exit(0);