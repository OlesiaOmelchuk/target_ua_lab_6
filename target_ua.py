"""Target game Ukrainian version"""
import random
from typing import List


def generate_grid() -> List[str]:
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


def get_words(path: str, letters: List[str]) -> List[str]:
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
    return words_list


def check_user_words(user_words: List[str], language_part: str, letters: List[str],
                     dict_of_words: List[str]) -> List[List[str]]:
    """
    Checks user's words. Returns list of right user's words and list of words\
which user didn't mention.
    """
    right_user_words = []
    for word in user_words:
        if 1 <= len(word) <= 5:
            if word[0] in letters:
                dict_length = len(dict_of_words)
                for i in range(dict_length):
                    if word == dict_of_words[i][0] and dict_of_words[i][1] == language_part:
                        right_user_words.append(word)

    other_words = [word[0] for word in dict_of_words if word[0]
                   not in right_user_words and word[1] == language_part]
    return right_user_words, other_words
