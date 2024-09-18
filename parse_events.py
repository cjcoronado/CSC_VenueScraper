import datetime
import re

# Import the functions from the files
from convert_to_date import convert_to_date
from clean_text import clean_text
from extract_event_name import extract_event_name
from extract_prices import extract_prices


def parse_events(soup):
    event_divs = soup.find_all('div', {'class': 'col-12 eventWrapper rhpSingleEvent py-4 px-0'})

    # Create an empty list to store each event's information
    event_info = []

    for div in event_divs:
        raw_date_line = div.find('div', {'class': 'mb-0 eventMonth singleEventDate text-uppercase'}).text

        # Use clean_text() to remove unneccessary characters
        cleaned_date_line = clean_text(raw_date_line)

        # Then, perform the split operation
        # Assuming cleaned_date_line = 'weekday month day',
        # ignore the first split element (weekday) with [1:]
        _, month, day = cleaned_date_line.split()

        # rest of the code...
        formatted_date, weekday = convert_to_date(month, day)

        # rest of the code...

        event_name_lines = div.find('h2', {
            'class': 'font1by25 font1By5remMD marginBottom3PX lineHeight12 font1By75RemSM font1By5RemXS mt-md-0 mb-md-2'})
        guest_lines = div.find('h4', {'id': 'evSubHead'})
        event_detail = extract_event_name(event_name_lines, guest_lines)

        event_prices_line = div.find('span', text=re.compile(r'\$\d+'))
        event_prices_detail = extract_prices(event_prices_line)

        date_string = formatted_date.strftime('%m/%d/%Y') if isinstance(formatted_date,
                                                                        datetime.datetime) else formatted_date
        output = f"{date_string} - {event_detail} / {event_prices_detail}, {weekday}"

        # Append the output string to the event_info list
        event_info.append(output)

    # After going through all events, return the event_info list
    return event_info
