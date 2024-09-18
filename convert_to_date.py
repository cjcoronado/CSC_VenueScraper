import datetime


def convert_to_date(month, day, year=2024):
    convert_month = {
        'January': 1, 'Jan': 1,
        'February': 2, 'Feb': 2,
        'March': 3, 'Mar': 3,
        'April': 4, 'Apr': 4,
        'May': 5,
        'June': 6, 'Jun': 6,
        'July': 7, 'Jul': 7,
        'August': 8, 'Aug': 8,
        'September': 9, 'Sep': 9, 'Sept': 9,
        'October': 10, 'Oct': 10,
        'November': 11, 'Nov': 11,
        'December': 12, 'Dec': 12
    }
    try:
        date_month = convert_month[month]
        date_day = int(day)
        formatted_date = datetime.datetime(year, date_month, date_day)
        weekday = formatted_date.strftime("%A")
        return formatted_date, weekday
    except KeyError:
        print(f'Invalid month name: {month}')
        return None, 'unknown'
    except ValueError:
        print(f'Invalid day: {day}')
        return None, 'unknown'
