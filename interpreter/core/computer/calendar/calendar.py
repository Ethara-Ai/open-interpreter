import datetime
import platform
import subprocess

from ..utils.run_applescript import run_applescript, run_applescript_capture


makeDateFunction = """
on makeDate(yr, mon, day, hour, min, sec)
	set theDate to current date
	tell theDate
		set its year to yr
		set its month to mon
		set its day to day
		set its hours to hour
		set its minutes to min
		set its seconds to sec
	end tell
	return theDate
end makeDate
"""

class Calendar:
    def __init__(self, computer):
        self.computer = computer
        # In the future, we might consider a way to use a different calendar app. For now its Calendar
        self.calendar_app = "Calendar"

    def get_events(self, start_date=datetime.date.today(), end_date=None):
        """
        Fetches calendar events for the given date or date range.
        """
        pass

    def create_event(
        self,
        title: str,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        location: str = "",
        notes: str = "",
        calendar: str = None,
    ) -> str:
        """
        Creates a new calendar event in the default calendar with the given parameters using AppleScript.
        """
        pass

    def delete_event(
        self, event_title: str, start_date: datetime.datetime, calendar: str = None
    ) -> str:
        if platform.system() != "Darwin":
            return "This method is only supported on MacOS"

        # The applescript requires a title and start date to get the right event
        if event_title is None or start_date is None:
            return "Event title and start date are required"

        # If there is no calendar, lets use the first calendar applescript returns. This should probably be modified in the future
        if calendar is None:
            calendar = self.get_first_calendar()
            if not calendar:
                return "Can't find a default calendar. Please try again and specify a calendar name."

        script = f"""
        {makeDateFunction}
        set eventStartDate to makeDate({start_date.strftime("%Y, %m, %d, %H, %M, %S")})
        -- Open and activate calendar first
        tell application "System Events"
            set calendarIsRunning to (name of processes) contains "{self.calendar_app}"
            if calendarIsRunning then
                tell application "{self.calendar_app}" to activate
            else
                tell application "{self.calendar_app}" to launch
                delay 1 -- Wait for the application to open
                tell application "{self.calendar_app}" to activate
            end if
        end tell
        tell application "{self.calendar_app}"
            -- Specify the name of the calendar where the event is located
            set myCalendar to calendar "{calendar}"
            
            -- Define the exact start date and name of the event to find and delete
            set eventSummary to "{event_title}"
            
            -- Find the event by start date and summary
            set theEvents to (every event of myCalendar where its start date is eventStartDate and its summary is eventSummary)
            
            -- Check if any events were found
            if (count of theEvents) is equal to 0 then
                return "No matching event found to delete."
            else
                -- If the event is found, delete it
                repeat with theEvent in theEvents
                    delete theEvent
                end repeat
                save
                return "Event deleted successfully."
            end if
        end tell
        """

        stderr, stdout = run_applescript_capture(script)
        if stdout:
            return stdout[0].strip()
        elif stderr:
            if "successfully" in stderr:
                return stderr

            return f"""Error deleting event: {stderr}"""
        else:
            return "Unknown error deleting event. Please check event title and date."

    def get_first_calendar(self) -> str:
        # Literally just gets the first calendar name of all the calendars on the system. AppleScript does not provide a way to get the "default" calendar
        script = f"""
            -- Open calendar first
            tell application "System Events"
                set calendarIsRunning to (name of processes) contains "{self.calendar_app}"
                if calendarIsRunning is false then
                    tell application "{self.calendar_app}" to launch
                    delay 1 -- Wait for the application to open
                end if
            end tell
            tell application "{self.calendar_app}"
            -- Get the name of the first calendar
                set firstCalendarName to name of first calendar
            end tell
            return firstCalendarName
            """
        stdout = run_applescript_capture(script)
        if stdout:
            return stdout[0].strip()
        else:
            return None
