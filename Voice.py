'''
Created on Jan 9, 2016

@author: joshua
'''
import random;


class Voice(object):
    '''
    classdocs
    '''
    k = object;
    p = object;
    
    # A 2-D list of voices. The order is Bass, Tenor, Alto, Soprano.
    NUMBER_OF_VOICES = 4;
    noteNames = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];
    voices = [];
    chordNotes = [];
    

    def __init__(self, AnyKey, Progression):
        '''
        Constructor
        '''
        self.k = AnyKey;
        self.p = Progression;
        
        for num in range(0, len(self.p.prog)):
            self.chordNotes.append(self.p.prog[num].notes.split('/'));
        print("ChordNotes: " + str(self.chordNotes));
        
        for num in range(0, self.NUMBER_OF_VOICES):
            self.voices.append(self.createVoice());
        
    def createVoice(self):
        ans = [];
        for num in range(0, len(self.chordNotes)):
            print("num: " + str(num));
            ans.append(self.chordNotes[num][random.randint(0, len(self.chordNotes[num])-1)]);
            
        print("ans: " + str(ans));
        return ans;
    
    def checkDoubling(self):
        print("TODO");
        for voice in self.voices:
            
    
    def refine(self):
        print("TODO");
        self.checkDoubling();
        
    def getInterval(self, first, second):
        print("TODO");
        return abs(first - second);
        