import datetime

today = datetime.datetime.now()
print(today.strftime("%Y-%m-%d %H:%M:%S"))

birthday = datetime.date(1994, 7, 24)
print(birthday)

tdelta = datetime.timedelta(days=10)
print(today - tdelta)

print(today.month)
print(today.weekday())