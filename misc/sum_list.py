def list_sum(input_list):
    summed_value = 0
    # todo: Write a for loop that adds the elements
    # of input_list to the sum variable
    for item in input_list:
        summed_value += item

    return summed_value


# These test cases check the list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))
