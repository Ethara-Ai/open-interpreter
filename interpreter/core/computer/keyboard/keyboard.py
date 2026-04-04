import os
import platform
import time

from ...utils.lazy_import import lazy_import

# Lazy import of pyautogui
pyautogui = lazy_import("pyautogui")


class Keyboard:
    """A class to simulate keyboard inputs"""

    def __init__(self, computer):
        self.computer = computer

    def write(self, text, interval=None, delay=0.30, **kwargs):
        """
        Type out a string of characters with some realistic delay.
        """
        pass

    def press(self, *args, presses=1, interval=0.1):
        keys = args
        """
        Press a key or a sequence of keys.

        If keys is a string, it is treated as a single key and is pressed the number of times specified by presses.
        If keys is a list, each key in the list is pressed once.
        """
        time.sleep(0.15)
        pyautogui.press(keys, presses=presses, interval=interval)
        time.sleep(0.15)

    def press_and_release(self, *args, presses=1, interval=0.1):
        """
        Press and release a key or a sequence of keys.

        This method is a perfect proxy for the press method.
        """
        pass

    def hotkey(self, *args, interval=0.1):
        """
        Press a sequence of keys in the order they are provided, and then release them in reverse order.
        """
        pass

    def down(self, key):
        """
        Press down a key.
        """
        pass

    def up(self, key):
        """
        Release a key.
        """
        pass
