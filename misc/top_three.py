def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    s = sorted(input_list, reverse=True)
    return s[:3]


t3 = top_three([2, 3, 5, 6, 8, 4, 2, 1])
t3 = top_three([2, 33])
print(t3)