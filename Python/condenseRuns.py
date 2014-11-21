import os
from fileIO import *

def condenseRuns(genNumber):
    """Returns the results of every run in a given generation"""
    allResults = []
    for runNumber in range(100):                        # For every run in the generation
        resultList = readResult(genNumber,runNumber)    # Get the result of that run
        resultList.insert(0,runNumber)                  # Add the run number to it,
        allResults.append(resultList)                   # Then add it to the list
    return allResults

def getBestRuns(genNumber,numberOfRuns, returnFullResults = False):
    """Returns a list of integers representing the top numberOfRuns runs from the given generation"""
    results = condenseRuns(genNumber)
    bestRuns = []
    for run in range(numberOfRuns):
        bestResult = [-1,-1,-1]       # Initialize the result number
        for result in results:                      # Look for the best result
            if result not in bestRuns:              # No double counting runs
                if result[1] > bestResult[1]:       # If it got further,
                    bestResult = result             # it's the new best.
                elif result[1] == bestResult[1]:    # If it tied the best,
                    if result[2] < bestResult[2]:   # and did it faster,
                        bestResult = result         # it's the new best
        bestRuns.append(bestResult)                 # Add the best run to our list
    if returnFullResults:   # If they asked for everything,
        return bestRuns     # just give it to them
    else:                                   # If they didn't,
        return [run[0] for run in bestRuns] # strip the numbers off and return those 

def createCSV(genNumber):
    allResults = ["Run Number, Maximum X, Frame Reached\n"]
    results = getBestRuns(genNumber, 100, True)
    for line in results:
        line = str(line[0]) + ',' + str(line[1]) + ',' + str(line[2]) + '\n'
        allResults.append(line)
    writeCSV(allResults,"gen" + str(genNumber))

if __name__ == '__main__':
    for gen in range(11):
        createCSV(gen)
    combineCSVs(11)
    print getBestRuns(0,10)