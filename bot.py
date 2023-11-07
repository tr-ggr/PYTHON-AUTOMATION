import webbrowser
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import random



def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def human():
    return random.randint(1, 3)

def login():
    pyautogui.moveTo(1147, 586, human())
    click()
    pyautogui.typewrite(username, interval=0.1)
    pyautogui.press("tab")
    pyautogui.typewrite(password, interval=0.2)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

username = "LaineLover"
password = "IamStupid12"

    

webbrowser.open('https://www.delugerpg.com/login')

# pyautogui.displayMousePosition()

time.sleep(3)

login()

time.sleep(5)

pyautogui.scroll(-700)

