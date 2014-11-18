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
    pass

def createCSV():
    return  # This code doesn't work - it's only here in case we decide we want to be able to make .csv files again
    
    allResults = ["Run Number, Maximum X, Frame Reached\n"]
    
    outputFile = open(resultsPath + "../allResults.csv", 'w')  # Create a .csv
    outputFile.writelines(allResults)                          # Write the results
    outputFile.close()                                         # Close the file

if __name__ == '__main__':
    print condenseRuns(0)
