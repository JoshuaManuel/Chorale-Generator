'''
Created on Nov 29, 2015

@author: joshua
'''
from Chord import Chord; #@UnresolvedImport
import random;
import datetime;

class Progression(object):
    '''
    classdocs
    '''
    
    prog = [];
    
    #Chords ranked by importance
    first = [1];
    second = [5, 7];
    third = [4, 3];
    fourth = [6,2];
    
    
    
    #Probabilities of Markov state transitions, given the chord.
    chain = {
                   1: [first, second, second, third, fourth, fourth],
                   2: [first, second, third, third, third, third, fourth],
                   3: [first, second, second, second, third, third, fourth],
                   4: [first, first, second, second, third, fourth],
                   5: [first, first, first, second, third, fourth],
                   6: [first, first, second, second, third, third, third,fourth],
                   7: [first, first, first, first, second, third, fourth]
                   }
    
    
    def __init__(self, k, numChords):
        '''
        Constructor
        '''
        
        self.k = k;
        self.createProgression(numChords);
    def createProgression(self, numChords):
        print("Creating chord progressions!");
        #Using markov chains
        
        seed = datetime.datetime.now();
        random.seed(str(seed));
        
        #Each piece starts on root 1
        self.prog.append(Chord(self.k, 1));
        for num in range(0, numChords): # actually adds one extra chord (I) at the end.
            lastChord = self.prog[len(self.prog)-1];
            chainList = self.chain[lastChord.root];
            randNum = random.randint(0, len(chainList)-1);
            chosenRank = chainList[randNum];
            self.prog.append(Chord(self.k, chosenRank[random.randint(0, len(chosenRank)-1)]));
        self.prog.append(Chord(self.k, 1));
    def setProgression(self, prog):
        for num in range(0, len(prog)):
                self.prog.append(Chord(self.k, prog[num]));