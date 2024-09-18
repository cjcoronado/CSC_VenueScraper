import datetime


def extract_date(raw_date_line):
    convert_month = {
        'January': 1, 'Jan': 1,
        'February': 2, 'Feb': 2,
        'March': 3, 'Mar': 3,
        'April': 4, 'Apr': 4,
        'May': 5,
        'June': 6, 'Jun': 6,
        'July': 7, 'Jul': 7,
        'August': 8, 'Aug': 8,
        'September': 9, 'Sep': 9,
        'October': 10, 'Oct': 10,
        'November': 11, 'Nov': 11,
        'December': 12, 'Dec': 12
    }
    # Rest of the function as before ...

    # Print raw_date_line for debugging
    print(f'Debug: raw_date_line = {raw_date_line}')

    if raw_date_line is not None and hasattr(raw_date_line, 'get_text'):
        date_tokens = raw_date_line.get_text().strip().split(', ')

        if len(date_tokens) < 2:
            print('Missing date or improper format')
            return "Unknown Date", "Unknown day"

        try:
            date_info = date_tokens[1].strip().split(' ')
            if len(date_info) >= 2:
                date_month, date_day = date_info[0], int(date_info[1])
            else:
                print('Insufficient date information')
                return "Unknown Date", "Unknown day"

            date_month = convert_month[date_month]
            formatted_date = datetime.datetime(2024, date_month, date_day)
        except (KeyError, ValueError) as err:
            print('Invalid date information:', err)
            return "Unknown Date", "Unknown day"

        weekday = formatted_date.strftime("%A")
    else:
        print("No date information found for event.")
        formatted_date = "Unknown Date"
        weekday = "Unknown day"
    return formatted_date, weekday
