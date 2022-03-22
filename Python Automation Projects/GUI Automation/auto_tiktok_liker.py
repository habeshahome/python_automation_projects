from random import random
import pyautogui as mouse
import time
import random

time.sleep(3)
print(mouse.size())
print(mouse.position())


for i in range(5):
    mouse.moveTo(821, 509, 1)
    time.sleep(random.randint(1,5))
    mouse.doubleClick()
    time.sleep(2)
    mouse.scroll(-6)
    
