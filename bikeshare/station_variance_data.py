import csv
from datetime import datetime
from pprint import pprint

from station_lib_fns import duration_in_mins, type_of_user, print_first_point


def station_ids(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the ids of the start and end stations.
    """

    if city == 'NYC' or city == 'Chicago':
        from_station_id = datum['from_station_id']
        to_station_id = datum['to_station_id']
    elif city == 'Washington':
        from_station_id = datum['Start station number']
        to_station_id = datum['End station number']

    return from_station_id, to_station_id


def is_weekend(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns whether the trip occurred on a weekend

    :param datum:
    :param city:
    :return: True if on a weekend, False otherwise
    """

    if city == 'NYC':
        start = datum['starttime']
        d = datetime.strptime(start, '%m/%d/%Y %H:%M:%S')
    elif city == 'Chicago':
        start = datum['starttime']
        d = datetime.strptime(start, '%m/%d/%Y %H:%M')
    elif city == 'Washington':
        start = datum['Start date']
        d = datetime.strptime(start, '%m/%d/%Y %H:%M')

    weekday = d.weekday()

    if weekday == 5 or weekday == 6:
        return True
    else:
        return False


def condense_data_for_station_variance(in_file, out_file, city):
    """
    This function takes full data from the specified input file
    and writes the condensed data to a specified output file. The city
    argument determines how the input file will be parsed.
    :param in_file:
    :param out_file:
    :param city:
    :return:
    """

    # the age may be off by a year, depending on when the rider's actual birthday is
    # compared to when this is run
    current_year = datetime.now().year

    with open(out_file, 'w') as f_out, open(in_file, 'r') as f_in:
        # set up csv DictWriter object - writer requires column names for the
        # first row as the "fieldnames" argument
        out_colnames = ['is_same_station', 'is_weekend', 'duration', 'user_type', 'gender', 'birthyear', 'age']
        trip_writer = csv.DictWriter(f_out, fieldnames=out_colnames)
        trip_writer.writeheader()

        trip_reader = csv.DictReader(f_in)

        # collect data from and process each row
        for row in trip_reader:
            # set up a dictionary to hold the values for the cleaned and trimmed
            # data point
            new_point = {}

            duration = duration_in_mins(row, city)
            weekend = is_weekend(row, city)
            user_type = type_of_user(row, city)
            from_station_id, to_station_id = station_ids(row, city)

            birthyear = row['birthyear']

            if birthyear:
                new_point['birthyear'] = birthyear
                new_point['age'] = current_year - int(birthyear)

            new_point['is_same_station'] = from_station_id == to_station_id
            new_point['duration'] = duration
            new_point['is_weekend'] = weekend
            new_point['user_type'] = user_type
            new_point['gender'] = row['gender']

            trip_writer.writerow(new_point)


# city_info = {'Chicago': {'in_file': './data/chi_ex.csv',
#                          'out_file': './data/chiex-variance.csv'}}

city_info = {'Chicago': {'in_file': './data/Chicago-Divvy-2016.csv',
                         'out_file': './data/Chicago-station-variance.csv'}}

for city, filenames in city_info.items():
    in_file = filenames['in_file']
    out_file = filenames['out_file']
    condense_data_for_station_variance(in_file, out_file, city)
    print_first_point(out_file)
