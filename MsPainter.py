import os
import subprocess
import keyboard
import pyautogui
import time
import win32api, win32con
# Staple Values assuming 1980 x 1080 display
# todo automate this process / add scan function with PIL and autogui
OpenX = 1444
OpenY = 121
OkX = 685
OkY = 740
CloseX = 1266
CloseY = 276
# Pink Color Code
RED = 255
GREEN = 105
BLUE = 180
# Location of the color buttons
YRED = 629
YGREEN = 658
YBLUE = 697
X = 1250

def Click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def DClick(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def Write(word):
    pyautogui.write(word)


# MS Paint start-up
subprocess.Popen('mspaint.exe')
time.sleep(1)

def Open():
    time.sleep(0.1)
    Click(OpenX, OpenY)
    time.sleep(0.1)


def Ok():
    time.sleep(0.1)
    Click(OkX, OkY)
    time.sleep(0.1)


def Close():
    time.sleep(0.1)
    Click(CloseX, CloseY)
    time.sleep(0.1)


def Color(RED, GREEN, BLUE):
    time.sleep(0.5)
    DClick(X, YRED)
    Write(str(RED))
    time.sleep(0.5)
    DClick(X, YGREEN)
    Write(str(GREEN))
    time.sleep(0.5)
    DClick(X, YBLUE)
    Write(str(BLUE))


Open()
Color(RED=RED, GREEN=GREEN, BLUE=BLUE)
Ok()

time.sleep(1)
# P
Click(1266, 376)
pyautogui.dragTo(1266, 276)
pyautogui.dragTo(1316, 276)
pyautogui.dragTo(1316, 326)
pyautogui.dragTo(1266, 326)
# x
Click(1346, 376)
pyautogui.dragTo(1386, 326)
Click(1346, 326)
pyautogui.dragTo(1386, 376)
# I
Click(1416, 376)
pyautogui.dragTo(1466, 376)
Click(1441, 376)
pyautogui.dragTo(1441, 276)
Click(1416, 276)
pyautogui.dragTo(1466, 276)
# N
Click(1496, 376)
pyautogui.dragTo(1496, 276)
pyautogui.dragTo(1546, 376)
pyautogui.dragTo(1546, 276)
# K
Click(1576, 376)
pyautogui.dragTo(1576, 276)
Click(1576, 326)
pyautogui.dragTo(1626, 376)
Click(1576, 326)
pyautogui.dragTo(1626, 276)
# Y
Click(1666, 326)
pyautogui.dragTo(1666, 376)
Click(1666, 326)
pyautogui.dragTo(1636, 276)
Click(1666, 326)
pyautogui.dragTo(1696, 276)

