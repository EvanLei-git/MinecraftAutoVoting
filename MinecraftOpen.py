import pygetwindow as gw
import pyautogui
import time
from pywinauto import Application
from pywinauto import Desktop
import win32gui
import win32con
import win32com.client
import os,sys
import subprocess

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

def create_shortcut(shortcut_name, arguments=""):
    target_folder='UltimMC'
    target_exe='UltimMC.exe'
    shell = win32com.client.Dispatch("WScript.Shell")

    # Get the current working directory
    current_path = os.getcwd()

    # Specify the path for the new shortcut
    shortcut_path = os.path.join(current_path, f'{shortcut_name}.lnk')

    # Specify the target path and arguments
    target_path = os.path.join(current_path, target_folder, target_exe)
    arguments = f'-d "{os.path.join(current_path, target_folder)}" {arguments}'

    # Create the shortcut
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.Arguments = arguments
    shortcut.Save()

    print(f'Shortcut created at: {shortcut_path}')

def check_file_exists(shortcut_name):
    file_path_with_extension = shortcut_name + ".lnk"
    return os.path.exists(file_path_with_extension)

def open_file(file_path):
    try:
        subprocess.Popen([file_path], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)

        print(f"Opened {file_path} with the default associated program.")
    except Exception as e:
        print(f"Error opening {file_path}: {e}")


def wait_for_window(title_prefix, timeout=60):
    start_time = time.time()

    while time.time() - start_time < timeout:
        for window in gw.getAllTitles():
            if window.startswith(title_prefix):
                return True
        time.sleep(1)  # Wait for 1 second before checking again

    return False

def terminate_process(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            pid = proc.info['pid']
            process = psutil.Process(pid)
            process.terminate()
            print(f"Terminated process {process_name} with PID {pid}.")
            return True
    return False

def type_text_in_minecraft():

    shortcut_name = "Minemalia"

    if not check_file_exists(shortcut_name):
        create_shortcut('Minemalia', '-l "1.20.1" -s "play.minemalia.com"')

    time.sleep(1)
    open_file(shortcut_name +'.lnk')


    title_prefix = "Minecraft "
    if not wait_for_window(title_prefix):
        process_name_to_terminate = "UltimMC.exe"
        if terminate_process(process_name_to_terminate):
            print(f"Terminated {process_name_to_terminate}.")
        else:
            print(f"No process found with the name {process_name_to_terminate}.")
    else:
        print(f"A window with title starting with '{title_prefix}' has appeared.")



    time.sleep(5)

    # Wait for the Minecraft window to come to the front
    bring_minecraft_to_front()
    time.sleep(3)
    



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

    import json

    config_file_path = r'C:\\minecraftpass.json'
    # Initialize passmain to None
    passmain = None

    try:
        with open(config_file_path, 'r') as file:
            config_data = json.load(file)
            passmain = str(config_data.get('password'))
    except FileNotFoundError:
        print(f"Config file not found at: {config_file_path}")

    pyautogui.typewrite(passmain)
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
