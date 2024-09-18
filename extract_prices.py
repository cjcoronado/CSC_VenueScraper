import re


def extract_prices(event_prices_line):
    if event_prices_line is not None:
        event_prices = re.findall(r'\$\d+', event_prices_line.get_text().strip())
        event_prices_detail = ' - '.join(event_prices)
    else:
        event_prices_detail = "Price details not available"
    return event_prices_detail