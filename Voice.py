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
    
    
    NUMBER_OF_VOICES = 4;
    noteNames = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];
    # A 2-D list of voices. The order is Bass, Tenor, Alto, Soprano.
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
        #Force specific voicing for first and last chord
        lastNote = len(self.voices[0])-1
        
        self.voices[0][0] = 1;
        self.voices[1][0] = 3;
        self.voices[2][0] = 5;
        self.voices[3][0] = 1;
        
        self.voices[0][lastNote-1] = 5;
        self.voices[1][lastNote-1] = 2;
        self.voices[2][lastNote-1] = 7;
        self.voices[3][lastNote-1] = 5;
        
        self.voices[0][lastNote] = 1;
        self.voices[1][lastNote] = 3;
        self.voices[2][lastNote] = 5;
        self.voices[3][lastNote] = 1;
        
        print("v.voices: " + str(self.voices));
        
        
        
    def createVoice(self):
        ans = [];
        for chord in self.p.prog:
            ans.append(self.k.chordNotes[chord.root-1][random.randint(0,2)]);
        return ans;
    
    
    '''
    #Implement if enough time.
    
    def checkDoubling(self):
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
    
    def refine(self): #depends on only block chords to work. Otherwise, will need a new system.
        #Check intervals between notes
        self.checkInterval();
        self.checkDoubling();
        self.checkVoiceLeading();
        
    def getInterval(self, first, second):
        return abs(first - second);
    '''

        