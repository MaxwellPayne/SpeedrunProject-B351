"""Outputs a generation, waits for all workers to complete, 
chooses the best n runs from the generation, gives them to 
Chris, outputs the next generation"""
from time import sleep

from condenseRuns import getBestRuns
from fileIO import makeGen, readRun, writeRun, genDoneRunning, getConfig

CONFIG_TABLE = getConfig()

CURRENT_GEN_NUMBER = CONFIG_TABLE['currentGenNumber']
SURVIVORS_PER_GEN = CONFIG_TABLE['survivorsPerGen']

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
  global CURRENT_GEN_NUMBER, SURVIVORS_PER_GEN
  while True:
    # wait for generation to finish
    while not genDoneRunning(CURRENT_GEN_NUMBER):
      sleep(0.01)
    # sleep little bit longer to avoid race conditions
    # with workers who still may be writing to Results files
    sleep(0.1)
    
    bestRuns = getBestRuns(CURRENT_GEN_NUMBER, SURVIVORS_PER_GEN)
    
    # chris spawns a list of new runs based on the best from this gen
    nextGenRuns = chris(streamRunfiles(CURRENT_GEN_NUMBER, bestRuns))
    
    # a new generation is born from chris's mutations
    CURRENT_GEN_NUMBER += 1
    makeGen(CURRENT_GEN_NUMBER)
    
    # write all new runs to sperate files
    for runNum, runText in enumerate(nextGenRuns):
      writeRun(CURRENT_GEN_NUMBER, runNum, runText)
      
    # ...and loop
  
  
if __name__ == '__main__':
  _main()
