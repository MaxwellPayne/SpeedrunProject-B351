import os
from Genetic import *
from fileIO import *

def randomRuns():
    for runNumber in range(100):
        writeRun(0,runNumber,[str(random_segment()) + '\n' for line in range(2000)])

randomRuns()