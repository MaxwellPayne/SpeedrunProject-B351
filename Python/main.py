"""Outputs a generation, waits for all workers to complete, 
chooses the best n runs from the generation, gives them to 
Chris, outputs the next generation"""

from condenseRuns import condenseRuns
from fileIO import makeGen, readRun, writeRun

GEN_NUMBER = 0

def chris(list_of_good_runs):
  # INPUT: a list of strings, each of which is the entire mnemonic reader text from some good run
  # OUTPUT: a list of strings, each of which represents the entire mnemonic text of a new, mutated run
  pass



def _main():
  while True:
    # WAIT for .csv to exist
    good_runs = condenseRuns(GEN_NUMBER)
    
    # chris spawns a list of new runs
    next_gen_runs = chris([readRun(GEN_NUMBER, identifier_num) for identifier_num in good_runs])
    
    # a new generation is born from chris's mutations
    GEN_NUMBER += 1
    # setup the .config file
    makeGen(GEN_NUMBER, len(next_gen_runs))
    
    # write all new runs to sperate files
    for run_num, run_text in enumerate(new_gen_list):
      writeRun(GEN_NUMBER, run_num, run_text)
      
    # ...and loop
    
    
  
  
if __name__ == '__main__':
  _main()
