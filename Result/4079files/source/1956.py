import datetime
import time
from typing import Sequence

import arrow


def roundTime(dt=None, roundTo=60):
	"""Round a datetime object to any time laps in seconds
	dt : datetime.datetime object, default now.
	roundTo : Closest number of seconds to round to, default 1 minute.
	Author: Thierry Husson 2012 - Use it as you want but don't blame me.
	"""
	if dt == None:
		dt = datetime.datetime.now()
	seconds = (dt - dt.min).seconds
	# // is a floor division, not a comment on following line:
	rounding = (seconds + roundTo / 2) // roundTo * roundTo
	return dt + datetime.timedelta(0, rounding - seconds, -dt.microsecond)


def filter_datetimes(datetimes: Sequence[datetime.datetime], leeway: int, target_dt: datetime.datetime):
	ret = []
	target_dt = arrow.get(target_dt)  # type: arrow.Arrow
	for dt in datetimes:
		dt = arrow.get(dt)
		low = dt.replace(minutes=leeway*-1)
		high = dt.replace(minutes=leeway)
		if low <= target_dt <= high:
			ret.append(dt)
	return ret


def format_dt(dt: datetime.datetime):
	return dt.strftime('%m/%d/%Y %l:%M %p')


def sort_datetimes_by_closeness_to_datetime(datetimes: Sequence[datetime.datetime],
                                            closeness_dt: datetime.datetime) -> Sequence[datetime.datetime]:
	def get_key(dt):
		fixed_dt = dt.replace(year=closeness_dt.year, month=closeness_dt.month, day=closeness_dt.day)
		fixed_ts = time.mktime(fixed_dt.timetuple())
		search_ts = time.mktime(closeness_dt.timetuple())
		return abs(fixed_ts - search_ts)

	return sorted(datetimes, key=get_key)

def difference_in_minutes(dt1: datetime.datetime, dt2: datetime.datetime) -> int:
	d1_ts = time.mktime(dt1.timetuple())
	d2_ts = time.mktime(dt2.timetuple())
	return abs(int(d1_ts-d2_ts) / 60)