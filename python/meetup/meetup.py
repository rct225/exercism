from datetime import date
import calendar
import pdb


class MeetupDayException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def meetup_day(year, month, day_of_the_week, description):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']
    weekdays_dict = {k: v for v, k in enumerate(weekdays)}
    day_to_num = weekdays_dict[day_of_the_week]
    meetup_calendar = calendar.Calendar(0)
    calendar_month = meetup_calendar.monthdatescalendar(year, month)

    day_dates = [dates[day_to_num].day for dates in calendar_month]

    day_number = 0
    my_date = None

    try:
        if description == 'teenth':
            day_number = [i for i in day_dates if i > 12 and i < 20][0]
        elif description == 'last':
            offset = -1
            if day_dates[-1] < day_dates[-2]:
                offset = -2
            day_number = day_dates[offset]
        else:
            offset = 1
            if day_dates[0] > day_dates[1]:
                offset = 0
            day_number = day_dates[(int(description[0]) - offset)]
        my_date = date(year, month, day_number)
    except IndexError:
        raise MeetupDayException('')

    return my_date
