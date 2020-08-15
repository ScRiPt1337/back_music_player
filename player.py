import subprocess
import requests
from playsound import playsound
import random
import string
import tempfile, os, sys
import argparse
import threading
from pynput import keyboard

class Youtube():
    def __init__(self,url):
        self.url = url
        self.path = ""
        
    def formate(self):
        codes = []
        result = subprocess.check_output("youtube-dl -F " + self.url +  " --no-playlist", shell=True)
        for i in result.decode('utf-8').split("\n"):
            if "audio only" in i:
                try:
                    zx = i.split(" ")
                    for i in zx:
                        codes.append(int(i))
                except:
                    pass
        return codes
    
    
    def geturl(self, codes):
        result = subprocess.check_output("youtube-dl -f " + str(codes) + " " + self.url +  " --no-playlist --get-url", shell=True)
        return result.decode()
    
    def get_random_string(self,length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
    
 
def callmain(url):
    yt = Youtube(url)
    codes = yt.formate()
    playsound(yt.geturl(codes[-1]))

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='play background music from your terminal.')
        parser.add_argument('url', metavar='url', type=str, nargs='+',
                            help='Youtube url or local_file location')
        args = parser.parse_args()
        if args.url[0].startswith("https://"):
            x = threading.Thread(target=callmain, args=(args.url[0],))
        else:
            x = threading.Thread(target=playsound, args=(args.url[0],))
        x.setDaemon(True)
        x.start()
        COMBINATIONS = [
            {keyboard.Key.ctrl, keyboard.Key.shift ,keyboard.KeyCode(char='#')}
        ]
        current = set()

        def execute():
            sys.exit()

        def on_press(key):
            if any([key in COMBO for COMBO in COMBINATIONS]):
                current.add(key)
                if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
                    execute()

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        pass
