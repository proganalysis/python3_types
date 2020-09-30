from datetime import date, datetime, timedelta, tzinfo
from pytz import timezone, utc, all_timezones
from icalendar import Calendar
from dateutil.rrule import rrulestr, rruleset
from dateutil import tz
from tzlocal import get_localzone

# inspiration from
# https://www.nylas.com/blog/calendar-events-rrules/

# TODO deal with exceptions on dates
# TODO deal with cancellations
# TODO deal with reminders


def orgDatetime(dt, tz):
    """Timezone aware datetime to YYYY-MM-DD DayofWeek HH:MM str in localtime.
    """
    return dt.astimezone(tz).strftime("<%Y-%m-%d %a %H:%M>")


def orgDate(dt, tz):
    """Timezone aware date to YYYY-MM-DD DayofWeek in localtime.
    """
    return dt.astimezone(tz).strftime("<%Y-%m-%d %a>")


def org_interval(start, duration, tz):
    return "  {}--{}\n".format(
        orgDatetime(start, tz),
        orgDatetime(start + duration, tz),
    )


def put_tz(date_time):
    if not hasattr(date_time, 'hour'):
        return datetime(
            year=date_time.year,
            month=date_time.month,
            day=date_time.day,
            tzinfo=tz.tzlocal())
    return date_time.astimezone(tz.tzlocal())


class orgEntry:
    """Documentation for orgEntry"""

    def __init__(self, event):
        self.summary = event["SUMMARY"]
        self.dtstart = put_tz(event["DTSTART"].dt)
        if "DTEND" in event:
            self.dtend = put_tz(event["DTEND"].dt)
            self.duration = self.dtend - self.dtstart
        else:
            self.duration = event["DURATION"].dt

        self.tz = get_localzone()
        self.properties = {}
        self._get_properties(event)
        self.description = event[
            'DESCRIPTION'] if 'DESCRIPTION' in event else ''

        if "RRULE" in event:

            self.rule = rrulestr(
                event["RRULE"].to_ical().decode("utf-8"),
                dtstart=self.dtstart,
            )
        else:
            self.rule = ""

    def _get_properties(self, event):
        if "LOCATION" in event:
            self.properties.update({"location": event["LOCATION"].title()})

    @property
    def pbox(self):
        props = "\n".join(
            ":%s: %s" % (k.upper(), v) for k, v in self.properties.items())
        if props:
            return f""":PROPERTIES:\n{props}\n:END:\n"""
        return ""

    @property
    def dates(self):

        now = datetime.now(utc)
        start = now - timedelta(28)
        end = now + timedelta(90)

        if self.rule:
            return self.repeting_dates(start, end)

        if self.dtstart < end and self.dtstart > start:
            return org_interval(self.dtstart, self.duration, self.tz)

    def repeting_dates(self, start, end):

        repetitions = self.rule.between(after=start, before=end)
        dateblock = ""
        for event_start in repetitions:
            dateblock += org_interval(event_start, self.duration, self.tz)

        return dateblock

    def __str__(self):
        events = self.dates
        if events:
            return f"* {self.summary}\n{self.pbox}{events}{self.description}"
        return ""


#with open("/home/me/myevs.ics") as fid:
#cal = Calendar.from_ical(fid.read())
##
#
#for entry in cal.walk():
#if entry.name == "VEVENT":
#print(orgEntry(entry))
