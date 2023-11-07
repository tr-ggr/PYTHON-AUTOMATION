import webbrowser
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import random

def human():
    return random.uniform(0.7, 1)

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

keyboard.wait("esc")

pyautogui.hotkey("ctrl", "shift", "j")
time.sleep(human())
keyboard.press("tab")
time.sleep(human())
i = 0

while keyboard.is_pressed('esc') == False:

    if(i == 6):
        print("DONE")    
        keyboard.write('document.querySelector("#battle > div.notify_warning > a:nth-child(6)").click()')
        keyboard.press("enter")
        time.sleep(human())
        keyboard.write('document.querySelector("#battle > div.notify_done > a:nth-child(9)").click()')
        keyboard.press("enter")
        i = 0
        time.sleep(human())        

    keyboard.write('document.querySelector("#battle > form > div.center > input:nth-child(1)").click()')
    keyboard.press("enter")
    time.sleep(human())
    keyboard.write('document.querySelector("#attack > div.cardif > form > div.buttoncenter > input:nth-child(1)").click()')
    keyboard.press("enter")
    time.sleep(human())
    keyboard.write('document.querySelector("#attack > div > form:nth-child(5) > div > input:nth-child(1)").click()')
    keyboard.press("enter")
    time.sleep(human())
    i+=1
