import calendar
year=int(input("Enter the Year:"))
month=int(input("Enter the month"))
print(calendar.calendar(year))
print(calendar.month(year,month))  #To print a particular month only

"""

The calendar module in Python provides functionality for working with calendars. 
It allows you to output calendars and provides additional functions for working with dates and times.

Here are some of the common functions provided by the calendar module:

1.calendar(year, w=2, l=1, c=6) - Returns a year's calendar as a multi-line string.

2.month(year, month, w=2, l=1) - Returns a month's calendar as a multi-line string.

3.weekday(year, month, day) - Returns the day of the week (0-6, where Monday is 0) for a given date.

4.isleap(year) - Returns True if a year is a leap year, False otherwise.

5.leapdays(y1, y2) - Returns the number of leap years between the years y1 and y2.

"""