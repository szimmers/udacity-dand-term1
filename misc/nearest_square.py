def nearest_square(value):
    """
    finds highest square < value
    :param value:
    :return:
    """
    i = 1
    highest_square = 1
    done = highest_square > value

    while not done:
        i += 1
        square = i ** 2
        if square > value:
            done = True
        else:
            highest_square = square

    return highest_square


test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))
test2 = nearest_square(1)
print("expected result: 1, actual result: {}".format(test2))

# def nearest_square(limit):
#     answer = 0
#     while (answer+1)**2 < limit:
#         answer += 1
#     return answer**2
