import keyboard
from config import HOTKEY


def wait_for_trigger():
    print(f"Press {HOTKEY} to activate microphone...")
    keyboard.wait(HOTKEY)
    print("Activated.")