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