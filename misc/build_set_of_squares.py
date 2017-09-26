def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2


# todo: populate "squares" with the set of all of the integers less
# than 2000 that are square numbers

squares = set()
done = False
value = 2000

while not done:
    nearest = nearest_square(value)
    if nearest in squares or nearest == 0:
        done = True
    else:
        squares.add(nearest)
        value = nearest

print(squares)
