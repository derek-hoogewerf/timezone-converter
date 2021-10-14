import datetime
import pytz

tz_1 = pytz.timezone('Europe/London').localize(datetime.datetime(2019, 3, 30, 9, 15)).tzinfo
tz_2 = pytz.timezone('Europe/London').localize(datetime.datetime(2019, 3, 31, 9, 15)).tzinfo
tz_3 = pytz.timezone('Europe/London').localize(datetime.datetime(2019, 4, 1, 9, 15)).tzinfo

date1 = datetime.datetime(2019 , 4, 25, tzinfo = tz_1)
date2 = datetime.datetime(2019 , 4, 25, tzinfo = tz_2)
date3 = datetime.datetime(2019 , 4, 25, tzinfo = tz_3)

utc_date = datetime.datetime(2019, 4, 25, tzinfo = pytz.UTC)

print ("Date 1:   ", date1, date1.tzinfo) # Timezone returns Europe/London
print ("Date 2:   ", date1, date2.tzinfo) # Timezone returns Europe/London
print ("Date 3:   ", date1, date3.tzinfo) # Timezone returns Europe/London
print ("UTC date: ", utc_date, utc_date.tzinfo) # Timezone returns UTC

print (date1 > date2) # returns True
print (date2 > date3) # returns False
print (date3 > date1) # returns False

print('Is Summer time?')
print(date1, tz_1.dst(date1) != datetime.timedelta(0))
print(date2, tz_2.dst(date2) != datetime.timedelta(0))
print(date3, tz_3.dst(date3) != datetime.timedelta(0))
