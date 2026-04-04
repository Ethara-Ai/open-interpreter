import time
import warnings

from IPython.display import display
from PIL import Image

from ...utils.lazy_import import lazy_import
from ..utils.recipient_utils import format_to_recipient

# Lazy import of optional packages
try:
    cv2 = lazy_import("cv2")
except:
    cv2 = None  # Fixes colab error
np = lazy_import("numpy")
pyautogui = lazy_import("pyautogui")
plt = lazy_import("matplotlib.pyplot")


class Mouse:
    def __init__(self, computer):
        self.computer = computer

    def scroll(self, clicks):
        """
        Scrolls the mouse wheel up or down the specified number of clicks.
        """
        pass

    def position(self):
        """
        Get the current mouse position.

        Returns:
            tuple: A tuple (x, y) representing the mouse's current position on the screen.
        """
        pass

    def move(self, *args, x=None, y=None, icon=None, text=None, screenshot=None):
        """
        Moves the mouse to specified coordinates, an icon, or text.
        """
        pass

    def click(self, *args, button="left", clicks=1, interval=0.1, **kwargs):
        """
        Clicks the mouse at the specified coordinates, icon, or text.
        """
        pass

    def double_click(self, *args, button="left", interval=0.1, **kwargs):
        """
        Double-clicks the mouse at the specified coordinates, icon, or text.
        """
        pass

    def triple_click(self, *args, button="left", interval=0.1, **kwargs):
        """
        Triple-clicks the mouse at the specified coordinates, icon, or text.
        """
        pass

    def right_click(self, *args, **kwargs):
        """
        Right-clicks the mouse at the specified coordinates, icon, or text.
        """
        pass

    def down(self):
        """
        Presses the mouse button down.
        """
        pass

    def up(self):
        """
        Releases the mouse button.
        """
        pass


import math
import time


def smooth_move_to(x, y, duration=2):
    start_x, start_y = pyautogui.position()
    dx = x - start_x
    dy = y - start_y
    distance = math.hypot(dx, dy)  # Calculate the distance in pixels

    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > duration:
            break

        t = elapsed_time / duration
        eased_t = (1 - math.cos(t * math.pi)) / 2  # easeInOutSine function

        target_x = start_x + dx * eased_t
        target_y = start_y + dy * eased_t
        pyautogui.moveTo(target_x, target_y)

    # Ensure the mouse ends up exactly at the target (x, y)
    pyautogui.moveTo(x, y)
