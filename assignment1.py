#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Winter 2025
Program: assignment1.py 
Author: Kiran Dangi
The python code in this file (assignment1.py) is original work written by
Kiran Dangi. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or online resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and violators will be
reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    """
    Return the day of the week for a given date based on Tomohiko Sakamoto's algorithm.
    The result will be one of the following: 'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'.
    """
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year // 4 - year // 100 + year // 400 + offset[month] + date) % 7
    return days[num]

def leap_year(year: int) -> bool:
    """
    Check if a year is a leap year.
    A year is a leap year if it is divisible by 4, but not divisible by 100, unless divisible by 400.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """
    Return the maximum number of days in a given month of a given year.
    For example, February has 28 or 29 days depending on whether it's a leap year.
    """
    if month == 2:
        return 29 if leap_year(year) else 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 0  # Invalid month

def after(date: str) -> str:
    """
    Return the next day's date in the format YYYY-MM-DD.
    It handles leap years and month/year transitions correctly.
    """
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    tmp_day = day + 1

    if tmp_day > mon_max(month, year):
        to_day = 1
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month

    if tmp_month > 12:
        to_month = 1
        year += 1
    else:
        to_month = tmp_month

    next_date = f"{year}-{to_month:02}-{to_day:02}"
    return next_date

def valid_date(date: str) -> bool:
    """
    Validate if the given date string is in the correct format (YYYY-MM-DD) and represents a valid date.
    Returns True for valid dates, False otherwise.
    """
    try:
        parts = date.split('-')
        if len(parts) != 3:
            return False
        if not (parts[0].isdigit() and len(parts[0]) == 4):
            return False  # Year must be a 4-digit number
        year, month, day = map(int, parts)
        if month < 1 or month > 12:
            return False
        if day < 1 or day > mon_max(month, year):
            return False
        return True
    except:
        return False

def day_count(start_date: str, stop_date: str) -> int:
    """
    Calculate the number of weekend days (Saturdays and Sundays) between two given dates, inclusive.
    The function ensures that the dates are in correct order.
    """
    if start_date > stop_date:
        start_date, stop_date = stop_date, start_date

    count = 0
    current_date = start_date

    while current_date <= stop_date:
        y, m, d = map(int, current_date.split('-'))
        if day_of_week(y, m, d) in ['sat', 'sun']:
            count += 1
        current_date = after(current_date)

    return count

def usage():
    """
    Print the usage message and exit the program.
    This is called when the input arguments are incorrect.
    """
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit()

def main():
    """
    Main entry point of the script. It takes two date arguments and calculates the number of weekend days
    between them, then prints the result.
    """
    if len(sys.argv) != 3:
        usage()

    d1, d2 = sys.argv[1], sys.argv[2]

    if not valid_date(d1) or not valid_date(d2):
        usage()

    start, end = sorted([d1, d2])
    weekends = day_count(start, end)
    print(f"The period between {start} and {end} includes {weekends} weekend days.")

if __name__ == "__main__":
    main()
