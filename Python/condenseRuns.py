import os

def condenseRuns(genNumber):
    """Turns a directory full of runs into one .csv file"""
    allResults = ["Run Number, Maximum X, Frame Reached\n"]
    
    # Find and open the results
    dir = os.path.dirname(__file__)
    resultsPath = os.path.join(dir, "../Output/gen" + str(genNumber) + "/Results/")
    
    for fileNum, filename in enumerate(os.listdir(resultsPath)):            # Iterate
        resultFile = open(resultsPath + filename, 'r')                      # Open the file
        allResults.append(str(fileNum) + ',' + resultFile.readline()+'\n')  # Add the result to our list
        resultFile.close()                                                  # Close the file
    
    outputFile = open(resultsPath + "allResults.csv", 'w')  # Create a .csv
    outputFile.writelines(allResults)                       # Write the results
    outputFile.close()                                      # Close the file

condenseRuns(0)