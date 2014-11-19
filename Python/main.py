"""Outputs a generation, waits for all workers to complete, 
chooses the best n runs from the generation, gives them to 
Chris, outputs the next generation"""
from time import sleep

from condenseRuns import getBestRuns
from fileIO import makeGen, readRun, writeRun, genDoneRunning

# hardcoded; should these be tracked somewhere else?
GEN_NUMBER = 0
KEEPERS_PER_GEN = 5

def chris(stream_of_good_runs):
  # INPUT: a generator of strings, each of which is the entire mnemonic reader text from some good run
  # OUTPUT: a list of strings, each of which represents the entire mnemonic text of a new, mutated run
  raise NotImplementedError("function 'chris' is not a real function")

def streamRunfiles(genNumber, bestList):
  """returns generator that chris can iterate over
  to read the contents of the best files"""
  for runNumber in bestList:
    yield readRun(genNumber, runNumber)


def _main():
  global GEN_NUMBER, KEEPERS_PER_GEN
  while True:
    # wait for generation to finish
    while not genDoneRunning(GEN_NUMBER):
      sleep(0.01)
    # sleep little bit longer to avoid race conditions
    # with workers who still may be writing to Results files
    sleep(0.1)

    bestRuns = getBestRuns(GEN_NUMBER, KEEPERS_PER_GEN)

    # chris spawns a list of new runs based on the best from this gen
    nextGenRuns = chris(streamRunfiles(GEN_NUMBER, bestRuns))
    
    # a new generation is born from chris's mutations
    GEN_NUMBER += 1
    makeGen(GEN_NUMBER)
    
    # write all new runs to sperate files
    for runNum, runText in enumerate(nextGenRuns):
      writeRun(GEN_NUMBER, runNum, runText)
      
    # ...and loop
  
  
if __name__ == '__main__':
  _main()
