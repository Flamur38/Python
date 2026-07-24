
from datetime import datetime

ts = '2026-07-21 14:32:07'

parsed = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')    # string + pattern datetime object
print(parsed)           # 2026-07-21 14:32:07
print(type(parsed))     # <class 'datetime.datetime'>
                           


# Once parsed, datetimes behave like numbers:
first = datetime.strptime('2026-07-21 14:32:01', '%Y-%m-%d %H:%M:%S')
last = datetime.strptime('2026-07-21 14:32:10', '%Y-%m-%d %H:%M:%S')

print(last > first)             # True
gap = last - first              # Subtraction gives a timedelta
print(gap)                      # 0:00:09
print(gap.total_seconds())      # 9.0   as a plain number



# Current time:
now = datetime.now()            # right now, as a datetime object
print(now)                      # 2026-07-23 22:10:51.349438
