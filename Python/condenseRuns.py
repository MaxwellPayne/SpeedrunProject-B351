import os
from fileIO import *

def condenseRuns(genNumber):
    """Returns the results of every run in a given generation"""
    allResults = []
    for runNumber in range(getRunsPerGen()):             # For ever run in the generation
        resultList = readResult(genNumber,runNumber)    # Get the result of that run
        resultList.insert(0,runNumber)                  # Add the run number to it,
        allResults.append(resultList)                   # Then add it to the list
    return allResults


def getBestRuns(genNumber,numberOfRuns):
    """Returns a list of integers representing the top numberOfRuns runs from the given generation"""
    results = condenseRuns(genNumber)
    results.sort(key=lambda x: x[2])            # Sort runs based on distance reached
    results.reverse()                           # Reverse so I can take the top N runs
    bestRuns = []
    if numberOfRuns == "completed":
        for i in results:
            if i[2] == 2000:                    # Will return only runs that reached the end of the level
                bestRuns.append(i)
    else:
        for i in range(0,numberOfRuns):         # Add run numbers of best runs to list
            run = results[i]
            runNum = run[0]
            bestRuns.append(runNum)
    return bestRuns

def createCSV():
    return  # This code doesn't work - it's only here in case we decide we want to be able to make .csv files again
    
    allResults = ["Run Number, Maximum X, Frame Reached\n"]
    
    outputFile = open(resultsPath + "../allResults.csv", 'w')  # Create a .csv
    outputFile.writelines(allResults)                          # Write the results
    outputFile.close()                                         # Close the file

if __name__ == '__main__':
    print condenseRuns(0)
    print getBestRuns(0,10)

