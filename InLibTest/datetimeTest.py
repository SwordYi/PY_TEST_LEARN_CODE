from datetime import *

now = date.today()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.isoweekday())

tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
next_week = now + timedelta(days=7)
print(tomorrow)
print(yesterday)
print(next_week)

now = datetime.today()
print(now)

now = datetime.now()
print(now)
print(now.date())
print(now.time())

next_hour = now + timedelta(hours=1)
print(next_hour)
