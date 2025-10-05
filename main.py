import json

import requests

from defs import ADDRESS
from defs import DATE
from defs import METHOD
from defs import PRAYER_TIMES
from defs import URL


def fetch_prayer_times(address=ADDRESS, date=DATE, method=METHOD, url=URL) -> dict:
    """
    Fetch prayer times from the Aladhan API for a specific address and method.

    :param address: Address for which to fetch prayer times
    :param date: Date string in 'DD-MM-YYYY' format
    :param method: Calculation method for prayer times
    :param url: API endpoint URL
    :return: Dictionary containing prayer times or None if an error occurs
    """

    # Parameters for the request
    params = {"address": ADDRESS, "method": METHOD}

    # append the date to the URL
    url = f"{url}{date}"

    try:
        # Make the GET request
        response = requests.get(url, params=params)

        # Check if request was successful
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            return data
        else:
            print(f"Error: API request failed with status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None


def get_prayer_times_for_date(prayer_data: dict) -> dict:
    """
    Extract prayer times from the dictionary.

    :param prayer_data: Dictionary containing the API response
    :return: Dictionary of prayer times for the specified date or None if not found
    """
    if prayer_data and "data" in prayer_data:
        timings = prayer_data["data"].get("timings", {})
        # now, remove all non-prayer keys
        # TODO: handle strings mismatch, API may return something different than expected
        for timing in list(timings.keys()):
            if timing not in PRAYER_TIMES:
                del timings[timing]

        if len(timings) != len(PRAYER_TIMES):
            print("Warning: Some prayer times are missing in the response")
        return timings
    else:
        print("Error: Invalid prayer data")
        return None


if __name__ == "__main__":
    prayer_data = fetch_prayer_times()
    current_prayer_times = get_prayer_times_for_date(prayer_data)
    if prayer_data:
        # Pretty print the JSON response
        print(json.dumps(current_prayer_times, indent=2))
    else:
        print("Failed to fetch prayer times.")
