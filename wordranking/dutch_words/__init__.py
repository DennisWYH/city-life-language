__version__ = '0.2.5'

import os


def get_ranked():
    path = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(path, 'dutch10000-utf8.txt')) as word_list:
        return word_list.read().splitlines()
