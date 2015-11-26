'''
Created on Nov 25, 2015

@author: joshua
'''

class SuperKey(object):
    '''
    classdocs
    '''
    # to get sharps, just move backwards over the list
    flats = ['b', 'e', 'a', 'd', 'g', 'c', 'f'];
    sharps = ['f', 'c', 'g', 'd', 'a', 'e', 'b'];
    legend = {'c': 0, 'd': 2, 'e': 4, 'f': -1, 'g': 1, 'a': 3, 'b': 5};
    notenames = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];
    notes = [];
    
    def __init__(self, key):
        '''
        Creates the notes array
        '''
        key = key[0].lower() + key[1:];
        
        
        if len(key) == 3:
            #get the notes
            index = -1;
            KS = 0;
            for i in range(0, 7):
                if (key[0] == self.notenames[i]):
                    index = i;
            if index > -1:
                for i in range(index, index + 7):
                    self.notes.append(self.notenames[i%7]);
                #get the sharps or flats (if any)
                KS = self.legend[self.notes[0]];
                if key[1] == 'b':
                    KS -= 7;
                if key[1] == '#':
                    KS += 7;
                if key[2] == 'm':
                    KS -= 3;
                print(KS);
                
                if KS < 0:
                    for letter in self.notes:
                        if letter in self.flats[0:abs(KS)]:
                            self.notes[self.notes.index(letter)] = letter + '-';
                if KS > 0:
                    for letter in self.notes:
                        if letter in self.sharps[0:abs(KS)]:
                            self.notes[self.notes.index(letter)] = letter + '+';
                print(self.notes);
            else:
                print("Invalid key!");
        else:
            print("Invalid key!");
            
    def n(self, index):
        return self.notes[index -1];

if __name__ == '__main__':
    a = SuperKey("C#M");