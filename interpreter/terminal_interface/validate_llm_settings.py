"""
I do not like this and I want to get rid of it lol. Like, what is it doing..?
I guess it's setting up the model. So maybe this should be like, interpreter.llm.load() soon!!!!!!!
"""

import os
import subprocess
import time

os.environ["LITELLM_LOCAL_MODEL_COST_MAP"] = "True"
import litellm
from prompt_toolkit import prompt

from interpreter.terminal_interface.contributing_conversations import (
    contribute_conversation_launch_logic,
)


def validate_llm_settings(interpreter):
    """
    Interactively prompt the user for required LLM settings
    """
    pass


def display_welcome_message_once(interpreter):
    """
    Displays a welcome message only on its first call.

    (Uses an internal attribute `_displayed` to track its state.)
    """
    pass
