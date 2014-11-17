"""This module will do all the interesting genetic algorithm stuff"""

import frameaction

def dummy_give_birth():
    """Returns a new genetic permutation.
    Right now just returns a static frame
    read in from file"""
    next_gen = []
    with open('SMW_Y1_test.txt', 'r') as f:
        for ln in f:
            next_gen.append(ln.rstrip())
    return next_gen

if __name__ == '__main__':
    pass
