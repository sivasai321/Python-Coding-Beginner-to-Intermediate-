# Python Program to get the Date and Time
import datetime
time_now=datetime.datetime.now()
print(time_now.strftime("Year:%Y Date:%D Time: %T"))

"""
In Python, the strftime() method is used to format date and time objects into a string representation. 
The name "strftime" stands for "string format time".
The strftime() method is available for date, datetime, and time objects, and it takes a format string as its argument. 
The format string is a string that contains special codes that are replaced with the corresponding parts of the date or time object. 
For example, the code %Y is replaced with the year, %m with the month, %d with the day, and so on.

"""