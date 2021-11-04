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
    >>> get_words("base.lst", ['щ'])
    [('щасні', 'noun'), ('щасно', 'adverb'), ('щастя', 'noun'), ('ще', 'adverb'), \
('щебет', 'noun'), ('щем', 'noun'), ('щемно', 'adverb'), ('щеня', 'noun'), ('щепа', 'noun'), \
('щерба', 'noun'), ('щигля', 'noun'), ('щипак', 'noun'), ('щипок', 'noun'), ('щипці', 'noun'), \
('щир', 'noun'), ('щирий', 'adjective'), ('щит', 'noun'), ('щиток', 'noun'), ('щі', 'noun'), \
('щіпка', 'noun'), ('щітка', 'noun'), ('щіть', 'noun'), ('щічка', 'noun'), ('щогла', 'noun'), \
('щодва', 'adverb'), ('щодві', 'adverb'), ('щодня', 'adverb'), ('щока', 'noun'), \
('щоніч', 'adverb'), \
('щораз', 'adverb'), ('щорік', 'adverb'), ('щотри', 'adverb'), ('щука', 'noun'), ('щуп', 'noun'), \
('щупак', 'noun'), ('щупик', 'noun'), ('щупля', 'noun'), ('щур', 'noun'), ('щурик', 'noun'), \
('щурка', 'noun'), ('щуря', 'noun'), ('щучий', 'adjective'), ('щучин', 'adjective'), \
('щучка', 'noun')]
    """
    words_list = []
    with open(path, 'r') as file:
        info = file.readlines()
    for line in info:
        parts = line.split(' ', 1)
        if 1 <= len(parts[0]) <= 5:
            if parts[0][0] in letters:
                if parts[1].startswith('/n') or parts[1].startswith('noun'):
                    words_list.append((parts[0], 'noun'))
                if parts[1].startswith('/v') or parts[1].startswith('verb'):
                    words_list.append((parts[0], 'verb'))
                if parts[1].startswith('/adj') or parts[1].startswith('adjective'):
                    words_list.append((parts[0], 'adjective'))
                if parts[1].startswith('adv'):
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
