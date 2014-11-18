import os

def makeGen(genNumber):
    """Creates a new generation"""
    pass

def readRun(genNumber,runNumber):
    """Reads a given run number from a given generation, and returns a list of strings (the input strings)"""
    # Find the file
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, "../Output/gen" + str(genNumber) + "/Runs/run" + str(runNumber) + ".txt")
    
    runFile = open(filename, 'r')           # Open the file
    lineList = runFile.read().splitlines()  # Read all lines into a list
    runFile.close()                         # Close the file
    
    return lineList

def writeRun(genNumber,runNumber,lineList):
    """Writes a given run number to a given generation, based on the passed list of strings (the inputs)"""
    # Find the file
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, "../Output/gen" + str(genNumber) + "/Runs/run" + str(runNumber) + ".txt")
    
    runFile = open(filename, 'w')   # Open the file
    runFile.writelines(lineList)    # Write the given lines
    runFile.close()                 # Close the file

def readResult(genNumber,runNumber):
    """Reads a given result number from a given generation, and returns a list where index 0 is the maximum X, and index 1 is the frame count"""
    # Find and open the results folder
    dir = os.path.dirname(__file__)
    resultsPath = os.path.join(dir, "../Output/gen" + str(genNumber) + "/Results/")
    
    #Build the path to the requested file
    fileName = resultsPath + "result" + str(runNumber) + ".txt"
    
    # Open the file, and read it to a string, then close the file
    resultFile = open(fileName, 'r')
    resultString = resultFile.readline()
    resultFile.close()
    
    # Split the string into a list, and turn the strings to ints
    resultList = resultString.split(',')
    resultList = map(int, resultList)
    
    # Return the list of ints
    return resultList

def getRunsPerGen():
    """Returns the number of runs to be performed in each generation"""
    # Temporary hack... please actually look at the headers for any of the config stuff, so we can move settings around in the file
    return 100