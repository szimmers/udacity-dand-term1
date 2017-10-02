import csv
from pprint import pprint


def read_data_for_variance_analysis(filename):
    """
    reads in the data for analyzing variance of station pickup/dropoff
    :param filename:
    :return:
    """
    with open(filename, 'r') as f_in:
        # set up csv reader object
        reader = csv.DictReader(f_in)

        items = []

        for row in reader:
            new_item = {'is_same_station': row['is_same_station'],
                        'is_weekend': row['is_weekend'],
                        'duration': float(row['duration']),
                        'user_type': row['user_type'],
                        'gender': row['gender'],
                        'birthyear': row['birthyear'],
                        'age': row['age']}

            items.append(new_item)

    return items


def str_to_bool(s):
    """
    csv files have strings for True and False, this converts them to bools.
    :param s:
    :return:
    """
    if s == 'True':
        return True
    elif s == 'False':
        return False
    else:
        raise ValueError


def convert_ratio_to_pct_for_display(value):
    """
    label function for turning a ratio into a % value to 1 decimal place
    :param value:
    :return:
    """
    return "{:.1f}%".format(value * 100)


def get_ratio_same_station_dropoff(rides, include_weekend_only=False, include_female_only=False, include_user_types="BOTH"):
    """
    given data for rides, return the ratio for which rides concluded at the start station
    :param rides:   the ride data
    :param include_weekend_only: should the ratio examine the rides on the weekend only
    :param include_female_only:    should the ratio examine the rides for females only
    :param include_user_types:  the type of riders to consider, either Subscriber, Customer, or BOTH.
    :return:
    """
    same_station_count = 0
    diff_station_count = 0

    for ride in rides:
        is_same_station = str_to_bool(ride.get('is_same_station', 'False'))
        is_weekend = str_to_bool(ride.get('is_weekend', 'False'))
        gender = ride.get('gender', 'Male')
        user_type = ride.get('user_type')

        ride_filtered_out = False

        if include_weekend_only and not is_weekend:
            ride_filtered_out = True

        if include_female_only and gender != 'Male':
            ride_filtered_out = True

        if include_user_types != 'BOTH':
            ride_filtered_out = user_type == include_user_types

        if not ride_filtered_out:
            if is_same_station:
                same_station_count += 1
            else:
                diff_station_count += 1

    if same_station_count == 0 or diff_station_count == 0:
        return 0

    return same_station_count / (same_station_count + diff_station_count)


def get_datapoints_gender_age(rides):
    """
    gets all the datapoints, but just gender and age, as a list. excludes those w/ missing data
    :param rides:
    :return:
    """
    data = []

    for ride in rides:
        gender = ride.get('gender')
        age = ride.get('age')

        if gender and age:
            data.append({'age': age, 'gender': gender})

    return data


def put_gender_age_datapoints_into_bins(data, binsize=5):
    """
    given datapoints with age and gender, separate into bins separated by gender and
    age bins of 5 years (by default). Ignores any ages > 100.
    :param data:    the ride data with age and gender
    :param binsize: the size, in years, of each bin. we'll plot ages 0-100
    :return:
    """

    # by default, we'll do 20 bins.
    num_bins = 100 // binsize

    # each bin is 5 years of age, by default. we'll toss any ages > 100. these will represent
    # counts of ages for that bin.
    male_bins = [0] * num_bins
    female_bins = [0] * num_bins

    for datum in data:
        age = int(datum['age'])
        gender = datum['gender']

        if 0 < age <= 100:
            bin_number = age // binsize
            if gender == 'Male':
                male_bins[bin_number] += 1
            elif gender == 'Female':
                female_bins[bin_number] += 1

    return (male_bins, female_bins)


# rides = read_data_for_variance_analysis('data/chiex-variance.csv')
# rides = read_data_for_variance_analysis('data/Chicago-station-variance.csv')
# pprint(rides)

# ratio_all = get_ratio_same_station_dropoff(rides)
# print('all:', convert_ratio_to_pct_for_display(ratio_all))
#
# ratio_weekend_only = get_ratio_same_station_dropoff(rides, True)
# print('weekend only', convert_ratio_to_pct_for_display(ratio_weekend_only))
#
# ratio_female_only = get_ratio_same_station_dropoff(rides, False, True)
# print('female only', convert_ratio_to_pct_for_display(ratio_female_only))
#
# ratio_subscribers_only = get_ratio_same_station_dropoff(rides, False, False, 'Subscriber')
# print('subscribers only', convert_ratio_to_pct_for_display(ratio_subscribers_only))
#
# ratio_customers_only = get_ratio_same_station_dropoff(rides, False, False, 'Customer')
# print('customers only', convert_ratio_to_pct_for_display(ratio_customers_only))

# pointdata = get_datapoints_gender_age(rides)
# male_bins, female_bins = put_gender_age_datapoints_into_bins(pointdata, 10)
#
# print(male_bins)
# print(female_bins)
