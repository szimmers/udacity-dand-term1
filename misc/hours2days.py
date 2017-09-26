def hours2days(hours):
    """
    returns a tuple of the number of days and hours
    :param hours:
    :return:
    """
    return hours // 24, hours % 24


print(hours2days(5))
print(hours2days(24))
print(hours2days(27))
