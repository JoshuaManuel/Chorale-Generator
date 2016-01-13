'''
Created on Nov 25, 2015

@author: joshua
'''

class AnyKey(object):
    '''
    classdocs
    '''
    flats = ['b', 'e', 'a', 'd', 'g', 'c', 'f'];
    sharps = ['f', 'c', 'g', 'd', 'a', 'e', 'b'];
    legend = {'c': 0, 'd': 2, 'e': 4, 'f': -1, 'g': 1, 'a': 3, 'b': 5};
    noteNames = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];
    majorQualities = ['M', 'm', 'm', 'M', 'M', 'm', 'd'];
    chords = [];
    chordNotes = [[1,3,5],[2,4,6],[3,5,7],[4,6,1],[5,7,2],[6,1,3],[7,2,4]];
    
    def __init__(self, key):
        '''
        Creates the notes array
        '''
        self.notes = [];
        #make first letter lowercase
        key = key[0].lower() + key[1:];
        if len(key) == 3:
            #get the notes
            index = -1;
            KS = 0;
            for i in range(0, 7):
                if (key[0] == self.noteNames[i]):
                    index = i;
            if index > -1:
                for i in range(index, index + 7):
                    self.notes.append(self.noteNames[i%7]);
                #get the sharps or flats (if any)
                KS = self.legend[self.notes[0]];
                if key[1] == 'b':
                    KS -= 7;
                if key[1] == '#':
                    KS += 7;
                if key[2] == 'm':
                    KS -= 3;
                
                if KS < 0:
                    for letter in self.notes:
                        if letter in self.flats[0:abs(KS)]:
                            self.notes[self.notes.index(letter)] = letter + '-';
                if KS > 0:
                    for letter in self.notes:
                        if letter in self.sharps[0:abs(KS)]:
                            self.notes[self.notes.index(letter)] = letter + '+';
                
                for i in range(0, 7):
                    self.chords.append(self.notes[i] + "/" + self.notes[(i + 2)% 7] + "/" + self.notes[(i + 4)% 7]);
                print(self.chords);
            else:
                print("Invalid key!");
        else:
            print("Invalid key!");
    #Accessor methods for typing convenience    
    def n(self, index):
        print("notes: " + str(self.notes));
        return self.notes[index -1];
    
    def c(self, index):
        return self.chords[index -1];
    
    def translate(self, notes): #notes is an array of numbers
        ans = "";
        for noteDegree in notes:
            ans += " " + self.n(noteDegree);
        return ans;
if __name__ == '__main__':
    a = AnyKey("C#M");