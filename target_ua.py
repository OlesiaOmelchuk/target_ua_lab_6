"""Target game Ukrainian version"""
import random


def generate_grid():
    """
    Generates list of letters
    """
    grid_list = []
    alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    while len(grid_list) < 5:
        letter = random.choice(alphabet)
        if letter not in grid_list:
            grid_list.append(letter)
    return grid_list


def get_words(path, letters):
    """
    Reads the file path. Checks the words with rules and returns a list of \
tuples: word and part of speech
    """
    words_list = []
    with open(path, 'r') as file:
        info = file.readlines()
    for line in info:
        parts = line.split(' ', 1)
        if 1 <= len(parts[0]) <= 5:
            if parts[0][0] in letters:
                if '/n' in parts[1] or 'noun' in parts[1]:
                    words_list.append((parts[0], 'noun'))
                if '/v' in parts[1] or 'verb' in parts[1]:
                    words_list.append((parts[0], 'verb'))
                if '/adj' in parts[1] or 'adj' in parts[1]:
                    words_list.append((parts[0], 'adjective'))
                if 'adv' in parts[1]:
                    words_list.append((parts[0], 'adverb'))
    print(words_list)


print(get_words('base.lst', ['щ']))


def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    Checks user's words. Returns list of right user's words and list of words\
which user didn't mention.
    """
    pass
