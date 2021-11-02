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
    pass



def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    Checks user's words. Returns list of right user's words and list of words\
which user didn't mention.
    """
    pass