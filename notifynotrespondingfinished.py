import win32gui
from playsound import playsound
import time
import os

os.chdir(r"C:\Scripts\Notifynotresponding")

class windowtitles():

    def __init__(self, debug=False) -> None:
        self.searchlist=["NOT RESPONDING","GET LATEST","GETTING VERSION","READING FILE REFERENCES"]
        self.windowlist = []
        self.soundinqueue = False
        self.dwelltime = 2
        self.debug = debug
        win32gui.EnumWindows(self.callback, self.windowlist)

    def callback(self, hwnd, custom_list):
        if win32gui.IsWindowVisible( hwnd ) and win32gui.GetWindowText(hwnd):
            custom_list.append((hwnd, win32gui.GetWindowText(hwnd)))
           
    def refreshwindowlist(self):
        self.windowlist = []
        win32gui.EnumWindows( self.callback, self.windowlist )
        return self.windowlist

    def check_exists(self):
        for handle, title in self.windowlist:
            for searchitem in self.searchlist:
                if searchitem in str(title).upper():
                    exists = True
                    while exists:
                        if win32gui.IsWindow(handle):
                            print('Found: "'+ title)
                            time.sleep(self.dwelltime)
                        if not self.soundinqueue:
                            self.queuesound()
                            return False
                        else: return True
                        

    
    def queuesound(self):
        time.sleep(self.dwelltime)
        self.soundinqueue = True
        triggertime = time.time()
        soundpath=os.getcwd() + r'\Windows 10 Notify.mp3'
        while self.check_exists():
            windowclass.refreshwindowlist()
            self.check_exists()
            time.sleep(1)

        print("wololoo")
        playsound(soundpath)
        self.soundinqueue=False





windowclass = windowtitles(debug=False)

if __name__ == '__main__':
    while True:
        windowclass.refreshwindowlist()
        windowclass.check_exists()
        time.sleep(2)





