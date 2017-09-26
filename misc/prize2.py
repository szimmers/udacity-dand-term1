def which_prize(points):
    prize = None
    no_prize_msg = 'Oh dear, no prize this time.'

    if points < 0:
        msg = no_prize_msg
    elif points < 50:
        prize = 'wooden rabbit'
    elif points < 150:
        msg = no_prize_msg
    elif points < 180:
        prize = 'wafer-thin mint'
    elif points < 200:
        prize = 'penguin'
    else:
        msg = no_prize_msg

    if prize:
        msgt = 'Congratulations! You have won a {}!'
        msg = msgt.format(prize)

    return msg


print(which_prize(8))
print(which_prize(-2))
print(which_prize(191))
print(which_prize(500))
