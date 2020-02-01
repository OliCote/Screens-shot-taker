import pyautogui
import time
from PIL import ImageGrab
from PIL import Image
import urllib3
from pynput.mouse import Button,Controller

from selenium import webdriver


def click(x,y):
    mouse = Controller()
    mouse.position = (x,y)
    mouse.click(Button.left,1)

def screenshots(slug):
    img = ImageGrab.grab(bbox=(577,49,1343,1040))
    bslash = "\\";
    img.save("C:\Dev\Projects\Screen-taker\screenshots"+ bslash + str(slug) + ".png")


def run():
    xPos = 1350
    yPos = 540
    page = 507
    while page < 508:
        screenshots(page)
        time.sleep(2)
        click(xPos,yPos)
        time.sleep(1)
        page += 1

run()

