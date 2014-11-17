import os
from time import sleep
from Queue import Queue

import algorithm

CHILDREN_PER_GENERATION = 50

def dispatch_lua(generation, child):
    with open(os.path.join('python-to-lua', str(generation), str(child))) as f:
        for frame in algorithm.dummy_give_birth():
            f.write('%s\n', frame)

def recieve_results(generation, child):
    with open(os.path.join('lua-to-python', str(generation), str(child))) as f:
        results = f.read()
    if not results: # lua not ready yet
        return None
    else: # lua ran simulation
        results = results.split('\n')
        progress, time_spent = results[0], results[1]
        print 'Made it %s far in %s time' % (progress, time_spent)
        


if __name__ == '__main__':
    pass
