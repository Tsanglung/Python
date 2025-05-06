#透過鍵盤控制按住與放開滑鼠左鍵
import pyautogui
import threading
from pynput import keyboard

clicking = False
clicking_lock = threading.Lock()

def clicker():
    while True:
        with clicking_lock:
            if not clicking:
                break
        pyautogui.click()
        pyautogui.sleep(0.1) 

def on_press(key):
    try:
        if key == keyboard.Key.f1:
            print("F1 pressed: start clicking")
            pyautogui.mouseDown()
        elif key == keyboard.Key.f2:
            print("F2 pressed: stop clicking")
            pyautogui.mouseUp()
        elif key == keyboard.Key.home:
            print("F3 pressed: exit")
            return False
    except AttributeError:
        pass

print("F1 start")
print("F2 stop")
print("Home shout down")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
