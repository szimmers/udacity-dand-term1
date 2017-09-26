def which_prize(points):
    won_prize = False

    if points < 0:
        msg = 'Oh dear, no prize this time.'
    elif points < 50:
        won_prize = True
        prize = 'wooden rabbit'
    elif points < 150:
        msg = 'Oh dear, no prize this time.'
    elif points < 180:
        won_prize = True
        prize = 'wafer-thin mint'
    elif points < 200:
        won_prize = True
        prize = 'penguin'
    else:
        msg = 'Oh dear, no prize this time.'

    if won_prize:
        msgt = 'Congratulations! You have won a {}!'
        msg = msgt.format(prize)

    return msg


print(which_prize(8))
print(which_prize(-2))
print(which_prize(191))
print(which_prize(500))
