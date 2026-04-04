import platform

from ..utils.run_applescript import run_applescript_capture


class Contacts:
    def __init__(self, computer):
        self.computer = computer

    def get_phone_number(self, contact_name):
        """
        Returns the phone number of a contact by name.
        """
        pass

    def get_email_address(self, contact_name):
        """
        Returns the email address of a contact by name.
        """
        pass

    def get_full_names_from_first_name(self, first_name):
        """
        Returns a list of full names of contacts that contain the first name provided.
        """
        pass
