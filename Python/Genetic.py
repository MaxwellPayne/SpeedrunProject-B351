import random
from frameaction import *


#Enum of moves in bit map
Up = 0
Dn = 1
Lt = 2
Rt = 3
Sl = 4
St = 5
Y = 6
B = 7
X = 8
A = 9
L = 10
R = 11

#For each individual move, maps move to a probality and actual string character
PROB_DIST = {
    Up: float(1)/10, 
    Dn: float(1)/10, 
    Lt: float(1)/10, 
    Rt: float(1)/10,  
    Y:  float(1)/10, 
    B:  float(1)/10, 
    X:  float(1)/10, 
    A:  float(1)/10, 
    L:  float(1)/10, 
    R:  float(1)/10 }

#creates a dictionary which maps ranges to a move
PROB_RANGES = dict()
lower = 0
for move in PROB_DIST:
    upper = lower + PROB_DIST[move]
    PROB_RANGES[(lower, upper)] = move
    lower = upper


#Probability that any string will be mutated
PROB_MUTATE_SEGMENT = .1
#probability that a random string will contain two moves
PROB_TWO_MOVES = .1



#given a strand as a list of strings and a natural number, returns a list of mutated strands
def mutate_batch(original, n):
    batch = list()
    #creates n mutated strands from the original and adds them to the list
    for i in range(n):
        mutation = mutate_strand(original)
        batch.append(mutation)

    return batch





#Given a list of strings, returns a mutated list (non-destructive)
def mutate_strand(original):
    #As to not destroy the original strand, make a copy
    strand = original.copy()
    #walk over each string in the list
    for segment in enumerate(strand):
        P = random.random()
        
        #with probability of PROB_MUTATE_SEGMENT, replace the given segment with a random one
        if P < PROB_MUTATE_SEGMENT:
            #generate mutation and replace in list
            mutation = random_segment()
            strand[segment[0]] = mutation

    #return the mutated list of strings
    return strand
            
     

#returns a random string of moves
def random_segment():
    P = random.random()
    move1 = None
    move2 = None
    F = Frame()

    #looks to see where the random number fits in the ranges 
    for pair in PROB_RANGES:
        if P >= pair[0] and P < pair[1]:
            move1 = PROB_RANGES[pair]

    F.add_buttons(move1)

    #possible to add a second move
    P = random.random()
    
    if P < PROB_TWO_MOVES:
        P = random.random()
        #search for new move
        for pair in PROB_RANGES:
            if P >= pair[0] and P < pair[1]:
                move2 = PROB_RANGES[pair]

    if move2:
        F.add_buttons(move2)

    return F


