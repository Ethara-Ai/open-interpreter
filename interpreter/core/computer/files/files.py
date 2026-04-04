import difflib

from ...utils.lazy_import import lazy_import

# Lazy import of aifs, imported when needed
aifs = lazy_import('aifs')

class Files:
    def __init__(self, computer):
        self.computer = computer

    def search(self, *args, **kwargs):
        """
        Search the filesystem for the given query.
        """
        pass

    def edit(self, path, original_text, replacement_text):
        """
        Edits a file on the filesystem, replacing the original text with the replacement text.
        """
        pass


def get_close_matches_in_text(original_text, filedata, n=3):
    """
    Returns the closest matches to the original text in the content of the file.
    """
    pass
