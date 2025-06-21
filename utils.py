"""Utility functions."""
import re
import inflect


_inflect_engine = inflect.engine()


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


_symbol_map = {
    '<': 'LessThan',
    '>': 'GreaterThan',
    '=': 'Equals',
    '%': 'Percent',
    '&': 'And',
    '$': 'Dollar',
    '#': 'Number',
    '@': 'At',
    '*': 'Star',
    '+': 'Plus'
}


def text_to_pascal(text):
    """
    Converts arbitrary text to a PascalCase python identifier.
    """
    words = []
    parts = re.findall(r'\d+|[a-zA-Z]+|.', text)
    for part in parts:
        if part.isdigit():
            number_words = _inflect_engine.number_to_words(int(part)).replace('-', ' ').replace(',', ' ').split()
            words.extend(word.capitalize() for word in number_words)
        elif part.isalpha():
            words.append(part.capitalize())
        elif part in _symbol_map:
            words.append(_symbol_map[part])
    pascal_case = ''.join(words)
    return pascal_case


def text_to_screaming_snake(text):
    """
    Converts arbitrary text to a SCREAMING_SNAKE_CASE python identifier.
    """
    words = []
    parts = re.findall(r'\d+|[a-zA-Z]+|.', text)
    for part in parts:
        if part.isdigit():
            number_words = _inflect_engine.number_to_words(int(part)).replace('-', ' ').replace(',', ' ').split()
            words.extend(word.upper() for word in number_words)
        elif part.isalpha():
            words.append(part.upper())
        elif part in _symbol_map:
            words.append(_symbol_map[part])
    pascal_case = '_'.join(words)
    return pascal_case


def pascal_to_snake(pascal_str):
    """
    Converts a PascalCase string to snake_case.
    """
    snake_str = re.sub(r'(?<!^)(?=[A-Z]|(?<=\D)\d+)', '_', pascal_str).lower()
    return snake_str
