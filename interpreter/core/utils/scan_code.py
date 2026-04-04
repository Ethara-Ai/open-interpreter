import os
import subprocess

from .temporary_file import cleanup_temporary_file, create_temporary_file

try:
    from yaspin import yaspin
    from yaspin.spinners import Spinners
except ImportError:
    pass


def scan_code(code, language, interpreter):
    """
    Scan code with semgrep
    """
    pass
