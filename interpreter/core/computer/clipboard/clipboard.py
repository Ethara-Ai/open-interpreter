import platform
from ...utils.lazy_import import lazy_import

# Lazy import of optional packages
pyperclip = lazy_import('pyperclip')

class Clipboard:
    def __init__(self, computer):
        self.computer = computer

        if platform.system() == "Windows" or platform.system() == "Linux":
            self.modifier_key = "ctrl"
        else:
            self.modifier_key = "command"

    def view(self):
        """
        Returns the current content of on the clipboard.
        """
        pass

    def copy(self, text=None):
        """
        Copies the given text to the clipboard.
        """
        pass

    def paste(self):
        """
        Pastes the current content of the clipboard.
        """
        pass
