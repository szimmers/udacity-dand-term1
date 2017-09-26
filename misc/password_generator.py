# Use an import statement at the top
import random

word_file = "data/words.txt"
word_list = []

# fill up the word_list
with open(word_file, 'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)


def generate_password(words):
    """
    generate a password by randomly stringing together 3 words from the input word list
    :param words:
    :return:
    """
    return ''.join(random.sample(words, 3))


print(generate_password(word_list))
