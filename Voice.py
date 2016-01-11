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
        for num in range(0, len(self.k.chordNotes)):
            ans.append(self.k.chordNotes[num][random.randint(0, len(self.k.chordNotes[num])-1)]);
            #ans.append(self.chordNotes[num][random.randint(0, len(self.chordNotes[num])-1)]);
            
        print("ans: " + str(ans));
        return ans;
    
    def checkDoubling(self):
        print("TODO");
        #make sure each note is done once, then last can be whatever.
        
    def checkInterval(self):
        score = 0;
        for note in self.voices[0]:
            for otherVoice in range(1, len(self.voices)):
                interval = self.getInterval(note, self.voices[otherVoice]);
                if interval > 3:
                    score -= interval - 3;
        return score;
    
    def checkVoiceLeading(self):
        print("TODO");
    
    def refine(self):
        print("TODO"); #depends on only block chords to work. Otherwise, will need a new system.
        #Check intervals between notes
        self.checkInterval();
        self.checkDoubling();
        self.checkVoiceLeading();
        
    def getInterval(self, first, second):
        return abs(first - second);
    

        