import platform
import subprocess


class Os:
    def __init__(self, computer):
        self.computer = computer

    def get_selected_text(self):
        """
        Returns the currently selected text.
        """
        pass

    def notify(self, text):
        """
        Displays a notification on the computer.
        """
        pass

    # Maybe run code should be here...?
