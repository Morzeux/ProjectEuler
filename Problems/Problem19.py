'''
Created on 15.5.2014

@author: Morzeux
'''

MONTHS = {1: ('Jan', 31),
          2: ('Feb', 28),
          3: ('Mar', 31),
          4: ('Apr', 30),
          5: ('May', 31),
          6: ('Jun', 30),
          7: ('Jul', 31),
          8: ('Aug', 31),
          9: ('Sep', 30),
          10: ('Oct', 31),
          11: ('Nov', 30),
          12: ('Dec', 31)}

DAYS = {1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'}

class Date(object):
    """ Date object. """
    def __init__(self, day, month, year, name_day):
        self.day = day
        self.month = month
        self.year = year
        self.name_day = name_day
        self.leap = self._detect_leap()

    def incr_date(self):
        """ Increments date. """
        self.name_day = self.name_day + 1 if self.name_day < 7 else 1
        if self.day < self._days_in_month():
            self.day += 1
        elif self.month < 12:
            self.day = 1
            self.month += 1
        else:
            self.day = 1
            self.month = 1
            self.year += 1
            self.leap = self._detect_leap()

    def _detect_leap(self):
        """ Checks if leap year. """
        if self.year % 100 == 0 and self.year % 400 == 0:
            return True
        elif self.year % 100 != 0 and self.year % 4 == 0:
            return True
        else:
            return False

    def _days_in_month(self):
        """ Returns number of days in single month. """
        if self.month == 2 and self.leap:
            return MONTHS[self.month][1] + 1
        else:
            return MONTHS[self.month][1]

    def make_copy(self):
        """ Returns copy of date. """
        return Date(self.day, self.month, self.year, self.name_day)

def get_month(month):
    """ Returns number of month. """
    for k, val in MONTHS.items():
        if val[0] == month:
            return k

    return None

def get_day(month):
    """ Returns number of day. """
    for k, val in DAYS.items():
        if val == month:
            return k

    return None

def detect_date(date, init_date):
    """ Computes date from init_date. """
    init_date = init_date.make_copy()
    month = get_month(date[1])
    while init_date.day != date[0] or init_date.month != month \
    or init_date.year != date[2]:
        init_date.incr_date()

    return init_date

def same_dates(date1, date2):
    """ Evaluates if dates are same. """
    if date1.day == date2.day and date1.month == date2.month \
    and date1.year == date2.year:
        return True
    else:
        return False

def problem(start=(1, 'Jan', 1901), finish=(31, 'Dec', 2000), day_nam='Sunday'):
    """
    You are given the following information, but you may prefer
    to do some research for yourself.

            1 Jan 1900 was a Monday.
            Thirty days has September,
            April, June and November.
            All the rest have thirty-one,
            Saving February alone,
            Which has twenty-eight, rain or shine.
            And on leap years, twenty-nine.
            A leap year occurs on any year evenly divisible by 4,
            but not on a century unless it is divisible by 400.

    How many Sundays fell on the first of the month
    during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    """

    init_date = Date(1, 1, 1900, 1)
    start = detect_date(start, init_date)
    end = detect_date(finish, start)
    day_name = get_day(day_nam)
    days = 0
    while not same_dates(start, end):
        if start.name_day == day_name and start.day == 1:
            days += 1
        start.incr_date()

    return days
