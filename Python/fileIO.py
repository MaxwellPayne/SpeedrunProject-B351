import os, copy

# absolute path to this module
_dir = os.path.dirname(os.path.abspath(__file__))
_configTable = None

def getConfig():
    """Returns a table of configuration setting name : value pairs"""
    global _configTable
    # return the cached global _configTable if already created
    if _configTable is None:
        settings = {}
        configFpath = os.path.join('..', 'Output', 'genConfig.config')
        # open the config file
        with open(configFpath, 'r') as configFile:
            for ln in configFile:
                # if not a blank line
                if ln.rstrip() != '':
                    # set setting strings as keys, ints as values
                    name, val = tuple(ln.rstrip().split(':'))
                    settings[name] = int(val)
        _configTable = settings
    # return a clone of the table so no module
    # can alter the config settings used by other modules
    return copy.copy(_configTable)


def makeGen(genNumber):
    """Creates a new generation directory structure if not exists"""
    genDirName = os.path.join(_dir, '..', 'Output', 'gen%d' % genNumber)
    # if gen{genNumber} directory does not exist, make it
    if not os.path.exists(genDirName):
        os.mkdir(genDirName)
        # then cd into it and make 'Runs' aand 'Results' subdirectories
        os.chdir(genDirName)
        os.mkdir('Runs')
        os.mkdir('Results')
        os.chdir(_dir)

def readRun(genNumber,runNumber):
    """Reads a given run number from a given generation, and returns a list of strings (the input strings)"""
    # Find the file
    filename = os.path.join(_dir, "../Output/gen" + str(genNumber) + "/Runs/run" + str(runNumber) + ".txt")
    
    runFile = open(filename, 'r')           # Open the file
    lineList = runFile.read().splitlines()  # Read all lines into a list
    runFile.close()                         # Close the file
    
    return lineList

def writeRun(genNumber,runNumber,lineList):
    """Writes a given run number to a given generation, based on the passed list of strings (the inputs)"""
    # Find the file
    filename = os.path.join(_dir, "../Output/gen" + str(genNumber) + "/Runs/run" + str(runNumber) + ".txt")
    
    runFile = open(filename, 'w')   # Open the file
    runFile.writelines(lineList)    # Write the given lines
    runFile.close()                 # Close the file

def readResult(genNumber,runNumber):
    """Reads a given result number from a given generation, and returns a list where index 0 is the maximum X, and index 1 is the frame count"""
    # Find and open the results folder
    resultsPath = os.path.join(_dir, "../Output/gen" + str(genNumber) + "/Results/")
    
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
    """Returns the number of runs to be performed in each generation from .config file"""
    return getConfig()['runsPerGen']

def genDoneRunning(genNumber):
    """Returns bool for whether or not all Results files have been created in generation genNumber"""
    resultsDir = os.path.join('..', 'Output', 'gen%d' % genNumber, 'Results')
    
    return len(os.listdir(resultsDir)) >= getRunsPerGen()

def writeCSV(lines,fileName):
    outputPath = os.path.join(_dir, "../Output/CSVs/")
    outputFile = open(outputPath + fileName + ".csv", 'w')  # Create a .csv
    outputFile.writelines(lines)                            # Write the results
    outputFile.close()                                      # Close the file

if __name__ == '__main__':
    print getRunsPerGen()
    print genDoneRunning(0)
    print getConfig()
    print getConfig()