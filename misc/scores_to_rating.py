def scores_to_rating(score1, score2, score3, score4, score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    # STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    # STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1, score2, score3, score4, score5) / 3

    # STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating


def convert_to_numeric(score):
    """
    converts input to a number
    """
    return float(score)


def sum_of_middle_three(score1, score2, score3, score4, score5):
    """
    lose the outliers and sum the rest
    """
    min_score = min(score1, score2, score3, score4, score5)
    max_score = max(score1, score2, score3, score4, score5)

    return score1 + score2 + score3 + score4 + score5 - min_score - max_score


def score_to_rating_string(score):
    """
    convert the score to a rating
    """
    if score < 1:
        return 'Terrible'
    elif score < 2:
        return 'Bad'
    elif score < 3:
        return 'OK'
    elif score < 4:
        return 'Good'
    elif score < 5:
        return 'Excellent'
    else:
        return 'Super-excellent'


print(scores_to_rating(1, 2, 3, 4, 5))
print(scores_to_rating(1, "2", 3, 4.0, 5))
print(scores_to_rating(1.002, "22", 3, 4.99999, 500))
