
from datetime import datetime

now = datetime.now()
print(now, '\n')
print(now.year, now.month, now.day, '\n')

delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
print(delta, '\n')
print(delta.days, delta.seconds, '\n')

start = datetime(2011, 1, 7)

from datetime import timedelta
print(start + timedelta(12), '\n')

print(start - 2*timedelta(12), '\n')