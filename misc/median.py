def median(numbers):
    numbers.sort()  # The sort method sorts a list directly, rather than returning a new sorted list

    if len(numbers) % 2:
        middle_index = int(len(numbers) / 2)
        return numbers[middle_index]
    else:
        right_index = len(numbers) // 2
        left_index = right_index - 1
        return (numbers[right_index] + numbers[left_index]) / 2


test1 = median([1, 2, 3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1, 2, 3, 4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))
