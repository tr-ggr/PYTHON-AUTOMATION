import webbrowser
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import random

def human():
    return random.randint(1,2)

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def Capture():
    pyautogui.hotkey("ctrl", "shift", "j")
    time.sleep(human())
    click(157, 1062)
    time.sleep(human())
    keyboard.write('document.querySelector("#catch").click()')
    keyboard.press("enter")
    time.sleep(human())
    keyboard.write('document.querySelector("#battle > form > div.center > input:nth-child(1)").click()')
    keyboard.press("enter")
    time.sleep(human())
    keyboard.write('document.querySelector("#attack > div.cardif > form > div.buttoncenter > input:nth-child(1)").click()')
    keyboard.press("enter")
    time.sleep(human())
    for i in range(6):
        keyboard.write('document.querySelector("#itemwrap > div:nth-child(1) > form > div.buttoncenter.clear > input:nth-child(2)").click()')
        keyboard.press("enter")
        time.sleep(1)
    time.sleep(human())
    keyboard.write('document.querySelector("#battle > div.infobox > a.btn.btn-primary").click()')
    keyboard.press("enter")
    time.sleep(human())
    pyautogui.hotkey("ctrl", "shift", "j")
    time.sleep(human())
    pyautogui.click()

keybrd = ["left", "up", "down", "right"]

keyboard.wait("esc")

while 1:
    if pyautogui.locateOnScreen('notcaught.png' , region = (1321, 597, 70, 50), confidence= 0.8) != None or pyautogui.locateOnScreen('notcaught.png' , region = (1106, 597, 70, 50), confidence= 0.8):
        if (pyautogui.pixel(1348, 608)[0] == 224 or pyautogui.pixel(1348, 608)[0] == 215) or pyautogui.pixel(1127, 611)[0] == 224 or pyautogui.pixel(1127, 611)[0] == 215 :
            print("Already Caught!")
            time.sleep(4)

        else:
            print("Not Caught!")
            Capture()
            time.sleep(4)

    else:
        print("No pokemon yet")
        time.sleep(0.5)

    
    keyboard.press(random.choice(keybrd))

    time.sleep(random.randint(1,5))

