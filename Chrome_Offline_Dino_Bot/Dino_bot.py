from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np
import keyboard

restart = [947,595]
dino = [581,606]

def Turn_On():
    pyautogui.click(restart)

def Check_Path():
    box = (dino[0]+55,dino[1],dino[0]+145,dino[1]+33)
    image = ImageGrab.grab(box)
    greyimage = ImageOps.grayscale(image)
    g = np.array(greyimage.getcolors())
    return(g.sum())

def Check_Score():
    box = (1312,499,1326,513)
    image = ImageGrab.grab(box)
    greyimage = ImageOps.grayscale(image)
    g = np.array(greyimage.getcolors())
    print("ACC:",g.sum())
    return g.sum()

def Check_Game_Over():
    box = (827,539,846,554)
    image = ImageGrab.grab(box)
    greyimage = ImageOps.grayscale(image)
    g = np.array(greyimage.getcolors())
    print("G:",g.sum())
    return g.sum()

def Acceleration(score, prev_delay):
    if score == 12574:
        delay = 0.1
    elif score == 7137:
        delay = 0.090
    elif score == 13157:
        delay = 0.090
    elif score == 13230:
        delay = 0.080 
    elif score == 451:
        delay = prev_delay
    else: 
        delay = prev_delay
    return delay

time.sleep(4)
Turn_On()
delay = 0.1

while(True):
    delay = Acceleration(Check_Score(),delay)
    print(delay)

    if(Check_Path()!=3225):
        time.sleep(delay)
        pyautogui.keyDown('space')

    if keyboard.is_pressed('q'):
        break

    if Check_Game_Over() == 9439:
        time.sleep(0.4)
        Turn_On()