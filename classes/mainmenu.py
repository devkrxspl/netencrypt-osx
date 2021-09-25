# Imports
import sys;
import npyscreen;
import curses;

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

        self.add(npyscreen.TitleFixedText, name = menu_title, relx = (x_max - 23) // 2, rely = y_max // 2 - 5);
        self.add(npyscreen.ButtonPress, name="[ Login ]", relx = (x_max - 14) // 2, rely = y_max // 2 - 3, when_pressed_function=self.login);
        self.add(npyscreen.ButtonPress, name="[ Exit  ]", relx = (x_max - 14) // 2, rely = y_max // 2 - 1, when_pressed_function=self.exit);
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
            notify.notify_confirm("  Failed to establish a connection to the server.", "", form_color="WHITE_BLACK", editw=1, width=x_max - 10, relx = 5);

    def exit(self):

        self.parentApp.switchForm(None);
        
        client.disconnect();
        terminal.exit();