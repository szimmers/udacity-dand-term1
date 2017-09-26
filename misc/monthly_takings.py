monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}


def total_takings(yearly_record):
    """
    calcs the takings for the year
    :param yearly_record:
    :return:
    """
    total = 0

    for month in yearly_record:
        monthly_takes = yearly_record[month]
        for event_take in monthly_takes:
            total += event_take

    return total


print(total_takings(monthly_takings))

# def total_takings(yearly_record):
#     #total is used to sum up the monthly takings
#     total = 0
#     for month in monthly_takings.keys():
#         #I use the Python function sum to sum up over
#         #all the elements in a list
#         total = total + sum(monthly_takings[month])
#     return total
