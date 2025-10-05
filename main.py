import requests
import json


URL = "https://api.aladhan.com/v1/timingsByAddress/04-10-2025"
ADDRESS = "Canada,Ottawa"
METHOD = 1  # Muslim World League Method

def fetch_prayer_times(url=URL, address=ADDRESS, method=METHOD) -> dict:
    """
    Fetch prayer times from the Aladhan API for a specific address and method.
    
    :param url: API endpoint URL
    :param address: Address for which to fetch prayer times
    :param method: Calculation method for prayer times
    :return: Dictionary containing prayer times or None if an error occurs
    """
    
    # Parameters for the request
    params = {
        "address": ADDRESS,
        "method": METHOD
    }
    
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
    Extract prayer times for a specific date from the API response.
    
    :param prayer_data: Dictionary containing the API response
    :param date: Date string in 'DD-MM-YYYY' format
    :return: Dictionary of prayer times for the specified date or None if not found
    """
    if prayer_data and "data" in prayer_data:
        timings = prayer_data["data"].get("timings", {})
        # now, remove all non-prayer keys
        prayer_keys = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"] 
        # TODO: handle strings mismatch, API may return something different than expected  
        for timing in list(timings.keys()):
            if timing not in prayer_keys:
                del timings[timing]
        
        if len(timings) != len(prayer_keys):
            print("Warning: Some prayer times are missing in the response")
        return timings
    else:
        print("Error: Invalid prayer data")
        return None
    
def main():
    prayer_data = fetch_prayer_times()
    current_prayer_times = get_prayer_times_for_date(prayer_data)
    if prayer_data:
        # Pretty print the JSON response
        print(json.dumps(current_prayer_times, indent=2))

if __name__ == "__main__":
    main()