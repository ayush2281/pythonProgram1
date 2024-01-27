# import a module named datetime to work with date as date objects.
# import datetime

# x = datetime.datetime.now()
# 1st. datetime is module , 2nd. datetime is object datetime ke andr bana hua 3rd.now function is calling

import datetime
x =datetime.datetime.now()#current date time
print(x)

#the date contain year,month,hour,minute,second,and microsecond

# Creating date object

print(datetime.datetime(2024,1,26))

       #Python Dates
# he method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
# %b Month name, short version Dec
# %B Month name, full version # December
# %m  Month as a number 01-12 12
# %y Year, short version, without century 18
# %Y Year, full version 2018
# %H Hour 00-23 17
# %I Hour 00-12 05
# %p AM/PM PM
# %M Minute 00-59  41


now = datetime.datetime.now() #current date time
year = now.strftime("%y")
# print(now)
print("year",year)