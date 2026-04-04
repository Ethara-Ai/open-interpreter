import os
import platform
import re
import subprocess

from ..utils.run_applescript import run_applescript, run_applescript_capture


class Mail:
    def __init__(self, computer):
        self.computer = computer
        # In the future, we should allow someone to specify their own mail app
        self.mail_app = "Mail"

    def get(self, number=5, unread: bool = False):
        """
        Retrieves the last {number} emails from the inbox, optionally filtering for only unread emails.
        """
        if platform.system() != "Darwin":
            return "This method is only supported on MacOS"

        too_many_emails_msg = ""
        if number > 50:
            number = min(number, 50)
            too_many_emails_msg = (
                "This method is limited to 10 emails, returning the first 10: "
            )
        # This is set up to retry if the number of emails is less than the number requested, but only a max of three times
        retries = 0  # Initialize the retry counter
        while retries < 3:
            read_status_filter = "whose read status is false" if unread else ""
            script = f"""
            tell application "{self.mail_app}"
                set latest_messages to messages of inbox {read_status_filter}
                set email_data to {{}}
                repeat with i from 1 to {number}
                    set this_message to item i of latest_messages
                    set end of email_data to {{subject:subject of this_message, sender:sender of this_message, content:content of this_message}}
                end repeat
                return email_data
            end tell
            """
            stdout, stderr = run_applescript_capture(script)

            # if the error is due to not having enough emails, retry with the available emails.
            if "Can’t get item" in stderr:
                match = re.search(r"Can’t get item (\d+) of", stderr)
                if match:
                    available_emails = int(match.group(1)) - 1
                    if available_emails > 0:
                        number = available_emails
                        retries += 1
                        continue
                break
            elif stdout:
                if too_many_emails_msg:
                    return f"{too_many_emails_msg}\n\n{stdout}"
                else:
                    return stdout

    def send(self, to, subject, body, attachments=None):
        """
        Sends an email with the given parameters using the default mail app.
        """
        pass

    def unread_count(self):
        """
        Retrieves the count of unread emails in the inbox, limited to 50.
        """
        pass

    # Estimate how long something will take to upload
    def calculate_upload_delay(self, attachments):
        try:
            total_size_mb = sum(
                os.path.getsize(os.path.expanduser(att)) for att in attachments
            ) / (1024 * 1024)
            # Assume 1 MBps upload speed, which is conservative on purpose
            upload_speed_mbps = 1
            estimated_time_seconds = total_size_mb / upload_speed_mbps
            return round(
                max(0.2, estimated_time_seconds + 1), 1
            )  # Add 1 second buffer, ensure a minimum delay of 1.2 seconds, rounded to one decimal place
        except:
            # Return a default delay of 5 seconds if an error occurs
            return 5

    def format_path_for_applescript(self, file_path):
        # Escape backslashes, quotes, and curly braces for AppleScript
        file_path = (
            file_path.replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("{", "\\{")
            .replace("}", "\\}")
        )
        # Convert to a POSIX path and quote for AppleScript
        posix_path = f'POSIX file "{file_path}"'
        return posix_path
