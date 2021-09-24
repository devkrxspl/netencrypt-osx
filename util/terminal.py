import subprocess;

def init():
    subprocess.Popen(['osascript', '-e', 'tell application \"Terminal\" to set background color of window 1 to {0, 0, 0, 0}'], shell=False, stdout=subprocess.DEVNULL);

def exit():
    subprocess.Popen(['osascript', '-e', 'tell application "Terminal" to close first window'], shell=False, stdout=subprocess.DEVNULL);