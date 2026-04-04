import re

from rich.box import MINIMAL
from rich.markdown import Markdown
from rich.panel import Panel

from .base_block import BaseBlock


class MessageBlock(BaseBlock):
    def __init__(self):
        super().__init__()

        self.type = "message"
        self.message = ""

    def refresh(self, cursor=True):
        # De-stylize any code blocks in markdown,
        # to differentiate from our Code Blocks
        content = textify_markdown_code_blocks(self.message)

        if cursor:
            content += "●"

        markdown = Markdown(content.strip())
        panel = Panel(markdown, box=MINIMAL)
        self.live.update(panel)
        self.live.refresh()


def textify_markdown_code_blocks(text):
    """
    To distinguish CodeBlocks from markdown code, we simply turn all markdown code
    (like '```python...') into text code blocks ('```text') which makes the code black and white.
    """
    pass
