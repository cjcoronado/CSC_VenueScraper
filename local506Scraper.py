# Import built-in libraries
import requests
from bs4 import BeautifulSoup

# Import custom functions
from parse_events import parse_events
from write_and_open_file import write_and_open_file  # import our function


def get_website_data(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
            'From': 'youremail@domain.com'
        }

        # Get the webpage content
        response = requests.get(url, headers=headers)
        # Check if the request was successful
        response.raise_for_status()  # This will raise an HTTPError if the response was unsuccessful
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None
    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def main():
    url = 'https://local506.com/events/'  # venue website

    # Suppose you have a function to get the webpage data
    soup = get_website_data(url)

    # Call parse_events to get the extracted event details
    event_results = parse_events(soup)

    # write event_results to file and open it
    content = "\n".join(event_results)  # join all events into a single string with newlines in between
    write_and_open_file('Local506.txt', content)


if __name__ == "__main__":
    main()
