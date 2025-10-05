# Get today's date in DD-MM-YYYY format to pass in as a parameter

import os
from datetime import datetime

import requests
from dotenv import load_dotenv

from defs import ADDRESS
from defs import DATE
from defs import METHOD
from defs import PRAYER_TIMES
from defs import URL


load_dotenv()

global current_date, current_time

current_date = datetime.now().strftime("%d-%m-%Y")

# Get the current time in HH:MM format
current_time = os.getenv("CURRENT_TIME", datetime.now().strftime("%H:%M"))


def fetch_prayer_times(address=ADDRESS, date=DATE, method=METHOD, url=URL) -> dict | None:
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
    url = f"{url}{current_date}"

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


def get_prayer_times(prayer_data: dict) -> dict | None:
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


def check_if_prayer_time(time, prayer_times) -> str | None:
    """
    Check if the current time matches any prayer time.

    :param current_time: Current time in 'HH:MM' format
    :param prayer_times: Dictionary of prayer times
    :return: Name of the prayer if it's time, else None
    """
    for prayer, time in prayer_times.items():
        if time == current_time:
            return prayer
    return None


def put_all_together() -> str:
    """
    Fetch prayer times, check if it's time for any prayer, and print the result.
    """
    message = ""
    prayer_data = fetch_prayer_times()
    current_prayer_times = get_prayer_times(prayer_data)
    prayer_to_pray_now = check_if_prayer_time(current_time, current_prayer_times)
    if prayer_to_pray_now:
        # Pretty print the JSON response
        message = f"Time to pray: {prayer_to_pray_now}"
    else:
        message = f"Noting to pray at {current_time}"

    print(message)
    return message


if __name__ == "__main__":
    put_all_together()
