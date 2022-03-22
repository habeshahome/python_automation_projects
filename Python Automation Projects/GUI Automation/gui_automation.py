# pyautogui requires tkinter to work
import pyautogui
import time

# mouse functions
print(pyautogui.size())

time.sleep(3)  # pausing python execution to get enough time to change cursor position
print(pyautogui.position())  # showing the current cursor co-ordinates

pyautogui.moveTo(200, 200, 2)  # It moves the cursor to specific coordinates
pyautogui.moveRel(300, 300, 2)  # It will move relative to current cursor position

# Clicks

# Scrolling
pyautogui.scroll(300)    # positive value = scroll up       negative value = scroll down
# Mouse up & down

