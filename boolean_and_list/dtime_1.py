from datetime import datetime, date
import pytz

now = datetime.now()
print(now)

# now1 = date.today()
# print(now1)
# datetime1 = datetime(year=2025, month=1, day=25)
# print(datetime1)

# print(datetime1.month)

# now_str = now.strftime("%d/%m/%Y")
# print(now_str)

# datetime2 = "26-01-2025"
# datetime3 = datetime.strptime(datetime2,"%d-%m-%Y")
# print(datetime3)
# print(datetime3.year)
# print(datetime3.month)

# Timezone
tz_new_york = pytz.timezone("Asia/Saigon")
datetime_newyork = datetime.now(tz_new_york)
print(datetime_newyork)

# Timezone Helsinki
tz_helsinki = pytz.timezone("Europe/Helsinki")
datetime_helsinki = datetime.now(tz_helsinki)
print(datetime_helsinki)