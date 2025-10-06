# Import libraries
import urllib.request # required for importing files from the web
import json # necessary to work with json files


# Upload a json file from an URL https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script

# Define the URL that you will use to get the info about bank holidays in UK
uk_bank_holidays_url = "https://www.gov.uk/bank-holidays.json"

# Get the json file from the web and convert it to python dictionary
with urllib.request.urlopen(uk_bank_holidays_url) as url: # Get the json file
    data = json.loads(url.read().decode()) # Convert the json file to a python list
    print(data) # print the resulting file


# Split strings in python: https://www.w3schools.com/python/ref_string_split.asp


def GetHolidaysInUK(data, region, include_holiday=False, include_date=False):

    """
    The function extracts the holiday information for the specific region in UK in 2025.

    Arguments:
        data (dict): the dictionary with the holiday information of three regions in UK (
        Northern Ireland, England and Walse and Scotland.
        
        region (string): the name of the region to extract holiday information.
        
        include_holidays (boolean): decides if to return the name of the holiday.
        
        include_date (boolean): decides if to return the date of the holiday.

    Returns:
        Returns the list of a specific holiday information depending on include_holidays and include_date 
        parameters. 
        )
    """


    # Retrieve all holiday events for the specified region
    events = data[region]["events"]
    # Create an empty variable to store holiday information
    region_holidays = []

    # Go through each holiday and extract specified info (the name of the holiday and date)
    for event in events:
        title = event["title"] # the name of the holiday
        date = event["date"] # Date (YYYY-MM-DD)

        date_list = date.split("-") # Split the date into year, month and day
        year = date_list[0] # Get the date of the holiday

        month_day = f"{date_list[1]}.{date_list[2]}" # Get the month and the day info

        # Only include holidays occurring in 2025
        if year == "2025":
            # Determine which information to include based on user preferences
            if include_holiday and include_date:
                region_holidays.append([title, month_day])
            elif include_holiday:
                region_holidays.append(title)
            elif include_date:
                region_holidays.append(month_day)

    return region_holidays


# Get the holidays in Northern Ireland
holidays_in_norethern_Ireland = GetHolidaysInUK(
    data, region = "northern-ireland", include_holiday = True, include_date = True)

# Print out the holidays in Northern Ireland
print("These are the holidays that happen in Northern Ireland in 2025:")
for holiday in holidays_in_norethern_Ireland:
    print(f" - {holiday[0]} - {holiday[1]}") # Print the name of the holiday followed by the date


scotland_holidays = GetHolidaysInUK(data, region = "scotland", include_holiday = True, include_date = False)
england_and_wales_holidays = GetHolidaysInUK(data, region = "england-and-wales", include_holiday = True, include_date = False)
northern_ireland_holidays = GetHolidaysInUK(data, region = "northern-ireland", include_holiday = True, include_date = False)


# The link on how to use sets https://stackoverflow.com/questions/15768757/how-to-construct-a-set-out-of-list-items-in-python
# The link on hot to use difference https://www.geeksforgeeks.org/python/python-set-difference/
only_in_Northern_Ireland = set(northern_ireland_holidays).difference(
    set(england_and_wales_holidays), set(scotland_holidays))
print("These are the holidays unique to Northern Ireland compared to other UK members:")
for holiday in only_in_Northern_Ireland:
    print(f" - {holiday}")
