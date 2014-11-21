import os
from Genetic import *
from fileIO import *

def randomRuns(runLength):
    for runNumber in range(100):
        writeRun(0,runNumber,[str(random_segment()) + '\n' for line in range(runLength)])
        
def simpleRuns(runLength):
    for runNumber in range(100):
        writeRun(0,runNumber,['|..|...r........|............|\n' for line in range(runLength)])

simpleRuns(5000)