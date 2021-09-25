# Imports
import threading
import npyscreen;

from util import terminal;
from util import encrypthandler;
from conn import client;

from classes import mainmenu;

# Classes
class App(npyscreen.NPSAppManaged):

    def onStart(self):

        # App Main
        sio = client.createClient();
        menu = mainmenu.MainMenu();

        self.registerForm("MAIN", menu);
        npyscreen.disableColor(); # Bad support for color, just disable
        terminal.init();

        # Socket Main
        threading.Thread(target=client.connectToServer).start();

# Main
app = App();
app.run();