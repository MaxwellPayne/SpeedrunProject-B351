"""Outputs a generation, waits for all workers to complete, 
chooses the best n runs from the generation, gives them to 
Chris, outputs the next generation"""
from time import sleep

import Genetic
from condenseRuns import getBestRuns
from fileIO import makeGen, readRun, writeRun, genDoneRunning, getConfig

CONFIG_TABLE = getConfig()

CURRENT_GEN_NUMBER = CONFIG_TABLE['currentGenNumber']
SURVIVORS_PER_GEN  = CONFIG_TABLE['survivorsPerGen']
RUNS_PER_GEN       = CONFIG_TABLE['runsPerGen'] 


def streamRunfiles(genNumber, bestList):
  """returns generator that chris can iterate over
  to read the contents of the best files"""
  for runNumber in bestList:
    yield readRun(genNumber, runNumber)


def _main():
  global CURRENT_GEN_NUMBER, SURVIVORS_PER_GEN
  print("Initializing...")
  while True:
    # wait for generation to finish
    print("Waiting for generation " + str(CURRENT_GEN_NUMBER) + " to finish.")
    while not genDoneRunning(CURRENT_GEN_NUMBER):
      sleep(0.01)
    # sleep little bit longer to avoid race conditions
    # with workers who still may be writing to Results files
    sleep(0.1)
    
    print("Getting the best runs from generation " + str(CURRENT_GEN_NUMBER) + ".")
    bestRuns = getBestRuns(CURRENT_GEN_NUMBER, SURVIVORS_PER_GEN)
    print("The best runs are: " + str(bestRuns))
    nextGenRuns = []
    # Genetic spawns a list of new runs based on the best from this gen
    print("Creating new runs...")
    for goodRun in streamRunfiles(CURRENT_GEN_NUMBER, bestRuns):
      nextGenRuns += Genetic.mutate_batch(goodRun, RUNS_PER_GEN / SURVIVORS_PER_GEN)
    
    # a new generation is born from Genetic's mutations
    CURRENT_GEN_NUMBER += 1
    makeGen(CURRENT_GEN_NUMBER)
    
    print("Writing new runs...")
    # write all new runs to separate files
    for runNum, runFrames in enumerate(nextGenRuns):
      writeRun(CURRENT_GEN_NUMBER, runNum, '\n'.join(map(str, runFrames)))
    
    print("Done writing runs.")
    # ...and loop
  
  
if __name__ == '__main__':
  _main()
