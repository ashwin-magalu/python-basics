import datetime
import pytz


''' I'm Doing this on 2nd Dec 2020 '''

today = datetime.date.today()
print(today)  # 2020-12-02

birthday = datetime.date(1994, 4, 26)
print(repr(birthday))  # datetime.date(1994, 4, 26)

days_since_birth = (today - birthday).days
print(str(days_since_birth) + " days")  # 9717 days

# This is 10 days ahead and behind to current day
tdelta = datetime.timedelta(days=10)
print(today + tdelta)  # 2020-12-12
print(today - tdelta)  # 2020-11-22

print(today.month)  # 12
print(today.day)  # 2
print(today.weekday())  # 2 => Wednesday = 2

print(datetime.time(12, 38, 20, 15))  # 12:38:20.000015
print(datetime.datetime(2020, 12, 2, 12, 38, 20, 15))
# 2020-12-02 12:38:20.000015

# This is 12 hours ahead to current day
hours_delta = datetime.timedelta(hours=12)
print(datetime.datetime.now() + hours_delta)  # 2020-12-03 00:44:24.321951

# pip install pytz using terminal
datetime_today = datetime.datetime.now(tz=pytz.UTC)
print(datetime_today)  # 2020-12-02 07:22:42.446393+00:00
datetime_pacific = datetime_today.astimezone(pytz.timezone("US/Pacific"))
print(datetime_pacific)  # 2020-12-01 23:22:14.102841-08:00

''' for tz in pytz.all_timezones:
    print(tz)  # gives all timezones names'''

# 2020-12-01 -> December 01 2020 f==> formatting
print(datetime_pacific.strftime('%B %d %Y'))  # December 01 2020

# December 01, 2020 -> datetime(2020-12-01) p ==> parsing
print(repr(datetime_pacific.strptime('December 01, 2020', '%B %d, %Y')))
# datetime.datetime(2020, 12, 1, 0, 0)

# Use https://github.com/timofurrer/maya instead of datetime, as it is easy and simple
