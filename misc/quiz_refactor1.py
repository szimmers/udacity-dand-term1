def is_submitted_answer_correct(submitted, correct):
    """
    indicates if the submitted answer matches the correct answer
    :param submitted:
    :param correct:
    :return:
    """
    return submitted == correct


def check_answers(my_answers, answers):
    """
    Checks the answers provided to a multiple choice quiz and returns the results.
    :param my_answers:
    :param answers:
    :return:
    """
    num_questions = len(answers)
    num_correct_answers = 0

    for i in range(len(answers)):
        correct_answer = answers[i]
        submitted_answer = my_answers[i]

        if is_submitted_answer_correct(submitted_answer, correct_answer):
            num_correct_answers += 1

    if num_correct_answers / num_questions > 0.7:
        return "Congratulations, you passed the test! You scored {} out of {}.".format(num_correct_answers, num_questions)
    else:
        return "Unfortunately, you did not pass. You scored {} out of {}.".format(num_correct_answers, num_questions)


answers = [5, 'foo', 'bear', -7, True]
my_answers = [5, 'foo', None, 'bar', 99]
print(check_answers(my_answers, answers))
