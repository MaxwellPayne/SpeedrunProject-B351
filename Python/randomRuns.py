import random
import os

def buildline():
    line = ''
    for button in range(12):
        button = random.choice('A.')
        line += button
    return line

def buildRuns():
    for runNumber in range(100):
        lineList = ['|..|' + buildline() + '|............|\n' for line in range(2000)]
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, "../Output/gen0/Runs/run" + str(runNumber) + ".txt")
        runFile = open(filename, 'w')
        runFile.writelines(lineList)