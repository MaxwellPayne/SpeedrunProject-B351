import argparse, re
from time import sleep

from termcolor import colored

class Speedrun(object):
    """Some class that will represent
    a single trial runthrough of SMW"""
    def __init__(self, runfile):
        with open(runfile, 'r') as f:
            self._moves = f.read().splitlines()

    @property
    def move_count(self):
        """Some calculated property we might
        someday care about"""
        return len(self.moves)

    @property
    def moves(self):
        """Each line of string is the
        combo of buttons pressed for that frame"""
        return re.sub('[-|.]', '', '\n'.join(self._moves))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genetic algorithms for Super Mario")
    parser.add_argument('runfile', nargs=1)

    args = parser.parse_args()
    runfile = args.runfile[0]

    run = Speedrun(runfile)
    
    messages = ["I am a child process",
                "Here is a sampling of the moves you did as specified by %s:" % runfile,
                run.moves[:50],
                "There were %d frames total" % run.move_count,
                "Ok Lua, have fun with that data I just gave you"]

    for m in messages:
        print colored(m, "cyan")

