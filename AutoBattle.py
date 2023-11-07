import webbrowser
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import random
from pynput.keyboard import Key, Listener

def human():
    return random.randint(1, 2)

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

keyboard.wait("esc")

pyautogui.hotkey("ctrl", "shift", "j")
time.sleep(human())
click(157, 1062)
time.sleep(human())

while keyboard.is_pressed('esc') == False:
    keyboard.write('document.querySelector("#battle > div.notify_warning > a:nth-child(5)").click()')
    keyboard.press("enter")
    time.sleep(human())
    keyboard.write('document.querySelector("#battle > div.notify_done > a.btn.btn-primary").click()')
    keyboard.press("enter")
    time.sleep(human())
    keyboard.write('document.querySelector("#battle > form > div.center > input:nth-child(1)").click()')
    keyboard.press("enter")
    time.sleep(human())
    keyboard.write('document.querySelector("#attack > div.cardif > form > div.buttoncenter > input:nth-child(1)").click()')
    keyboard.press("enter")
    time.sleep(human())
    keyboard.write('document.querySelector("#attack > div > form:nth-child(6) > div > input:nth-child(1)").click()')
    keyboard.press("enter")
    time.sleep(human())
    keyboard.write('document.querySelector("#attack > div > form:nth-child(5) > div > input:nth-child(1)").click()')
    keyboard.press("enter")
    time.sleep(human())
    
pyautogui.hotkey("ctrl", "shift", "j")
print("Done!")






