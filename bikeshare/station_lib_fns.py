import csv
from datetime import datetime
from pprint import pprint


def type_of_user(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the type of system user that made the
    trip.

    Remember that Washington has different category names compared to Chicago
    and NYC. NYC has some data points with a missing user type; you can leave
    these as they are (empty string).
    """

    if city == 'NYC' or city == 'Chicago':
        user_type = datum['usertype']
    elif city == 'Washington':
        dc_user_type = datum['Member Type']
        if dc_user_type == 'Registered':
            user_type = 'Subscriber'
        elif dc_user_type == 'Casual':
            user_type = 'Customer'

    return user_type


def time_of_trip(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the month, hour, and day of the week in
    which the trip was made.

    Remember that NYC includes seconds, while Washington and Chicago do not.

    HINT: You should use the datetime module to parse the original date
    strings into a format that is useful for extracting the desired information.
    see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    """

    if city == 'NYC':
        start = datum['starttime']
        d = datetime.strptime(start, '%m/%d/%Y %H:%M:%S')
        month = int(d.strftime('%m'))
        hour = int(d.strftime('%H'))
        day_of_week = d.strftime('%A')
    elif city == 'Chicago':
        start = datum['starttime']
        d = datetime.strptime(start, '%m/%d/%Y %H:%M')
        month = int(d.strftime('%m'))
        hour = int(d.strftime('%H'))
        day_of_week = d.strftime('%A')
    elif city == 'Washington':
        start = datum['Start date']
        d = datetime.strptime(start, '%m/%d/%Y %H:%M')
        month = int(d.strftime('%m'))
        hour = int(d.strftime('%H'))
        day_of_week = d.strftime('%A')

    return (month, hour, day_of_week)


def duration_in_mins(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the trip duration in units of minutes.

    Remember that Washington is in terms of milliseconds while Chicago and NYC
    are in terms of seconds.

    HINT: The csv module reads in all of the data as strings, including numeric
    values. You will need a function to convert the strings into an appropriate
    numeric type when making your transformations.
    see https://docs.python.org/3/library/functions.html
    """

    if city == 'NYC' or city == 'Chicago':
        duration_in_s = int(datum['tripduration'])
        duration = duration_in_s / 60.0
    elif city == 'Washington':
        duration_in_ms = int(datum['Duration (ms)'])
        duration = duration_in_ms / 1000 / 60.0

    return duration


def print_first_point(filename):
    """
    This function prints and returns the first data point (second row) from
    a csv file that includes a header row.
    """
    # print city name for reference
    city = filename.split('-')[0].split('/')[-1]
    print('\nCity: {}'.format(city))

    with open(filename, 'r') as f_in:
        ## TODO: Use the csv library to set up a DictReader object. ##
        ## see https://docs.python.org/3/library/csv.html           ##
        trip_reader = csv.DictReader(f_in)

        ## TODO: Use a function on the DictReader object to read the     ##
        ## first trip from the data file and store it in a variable.     ##
        ## see https://docs.python.org/3/library/csv.html#reader-objects ##
        first_trip = trip_reader.__next__()

        ## TODO: Use the pprint library to print the first trip. ##
        ## see https://docs.python.org/3/library/pprint.html     ##
        pprint(first_trip)

    # output city name and first trip for later testing
    return (city, first_trip)
