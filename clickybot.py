#!/usr/bin/env python3
# uses pyautogui to script clicks on an interface
# I use it to keep sessions alive when I can't keep an eye on something 
# pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org pyautogui

import sys
import time
import pyautogui

class clicky(object):
    _registered_clicky = []
    def __init__(self,name,mouse_coordinates):
        self._registered_clicky.append(self)
        self.name = name
        self.coordinates = mouse_coordinates

def main():
    def loop_away():
        print("Starting to loop in 10 Seconds!")
        time.sleep(10)
        while True:
            for c in clicky._registered_clicky:
                pyautogui.click(c.coordinates)
                print(f"Clicked on {c.name}")
                time.sleep(60)

    while True:
        print("Type 'done' to stop picking postions")
        name=input("One word name for clickable position: ")
        if name.lower()[:4] == 'done':
            if clicky._registered_clicky == []:
                print("no clicky things to click... exiting")
                sys.exit()
            else:
                loop_away()
        print("You have 6 seconds to move the mouse to that position ")
        time.sleep(6)
        mouse_coordinates = pyautogui.position()
        print(f"Captured position at {mouse_coordinates}")
        name = clicky(name, mouse_coordinates)

if __name__=="__main__":
    main()
