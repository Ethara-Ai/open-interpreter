import os

from .subprocess_language import SubprocessLanguage


class AppleScript(SubprocessLanguage):
    file_extension = "applescript"
    name = "AppleScript"

    def __init__(self):
        super().__init__()
        self.start_cmd = [os.environ.get("SHELL", "/bin/zsh")]

    def preprocess_code(self, code):
        """
        Inserts an end_of_execution marker and adds active line indicators.
        """
        pass

    def add_active_line_indicators(self, code):
        """
        Adds log commands to indicate the active line of execution in the AppleScript.
        """
        pass

    def detect_active_line(self, line):
        """
        Detects active line indicator in the output.
        """
        pass

    def detect_end_of_execution(self, line):
        """
        Detects end of execution marker in the output.
        """
        pass
