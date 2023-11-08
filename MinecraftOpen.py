import pygetwindow as gw
import pyautogui
import time
from pywinauto import Application
from pywinauto import Desktop

import win32gui
import win32con

def click_and_hold(x, y, duration=1):
    pyautogui.moveTo(x, y)  # Move the mouse cursor to the target position

    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()
def bring_minecraft_to_front():
    # Find a window with a title starting with "Minecraft"
    minecraft_window = None
    for window in Desktop(backend="uia").windows():
        if window.window_text().startswith("Minecraft "):
            minecraft_window = window
            break

    if minecraft_window:
        minecraft_window.set_focus()
        minecraft_window.maximize()

def type_text_in_minecraft():
    time.sleep(1)
    # Wait for the Minecraft window to come to the front
    bring_minecraft_to_front()
    time.sleep(2)
    

    # Rest of yo/test1 huhur typing function
    # Get the screen size
    width, height = pyautogui.size()
    
    # Calculate the middle of the screen
    middle_x = width // 2
    middle_y = height // 2




    #Back To Game button Cords
    # Mouse position: x = 967, y = 345
    pyautogui.click(967, 345)
    time.sleep(1)  # Optional delay between clicks

    pyautogui.press('2')
    time.sleep(1) 
    # Press the '/' key
    pyautogui.press('/')

    pyautogui.keyDown('backspace')  # Press and hold the Backspace key
    time.sleep(2)  # Keep the Backspace key pressed for the specified duration
    pyautogui.keyUp('backspace')  # Release the Backspace key


    time.sleep(1) 
    pyautogui.typewrite()
    pyautogui.press('enter')

    time.sleep(1)
    pyautogui.keyDown('w')  # Press the "W" key
    time.sleep(2)  # Keep the "W" key pressed for 2 seconds
    pyautogui.keyUp('w')  

    
    pyautogui.press('1')
    time.sleep(1)

    pyautogui.leftClick() # to right click on the Server Option Before choosing survival
    time.sleep(3)  # Optional delay between clicks


    # Survival SMPs button Cords
    # Mouse position: x = 677, y = 261
    click_and_hold(677, 261, duration=2)
    time.sleep(2)  # Optional delay between clicks

    # Survival Red button Cords
    # Mouse position: x = 1186, y = 334
    click_and_hold(1186, 334, duration=2)
    time.sleep(1)  # Optional delay between clicks

if __name__ == "__main__":
    type_text_in_minecraft()




#Back To Game button Cords
#Mouse position: x = 967, y = 345

#Survival SMPs button Cords
#Mouse position: x = 677, y = 261


#Survival Red button Cords
#Mouse position: x = 1186, y = 334   




'''
import time
import pyautogui

def get_mouse_position():
    while True:
        x, y = pyautogui.position()
        print(f"Mouse position: x = {x}, y = {y}")
        time.sleep(2)

if __name__ == "__main__":
    try:
        get_mouse_position()
    except KeyboardInterrupt:
        print("\nMouse position script terminated.")
'''