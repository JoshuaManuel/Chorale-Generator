'''
Created on Nov 29, 2015

Although not currently needed, this class is included to make future versions more extensible.

@author: joshua
'''

from AnyKey import AnyKey; #@UnresolvedImport

class Chord(object):
    '''
    classdocs
    '''
    #for minor, start on the 6th scale degree
    majorChords = ['M', 'm', 'm', 'M', 'M', 'm', 'd'];
    quality = None;
    notes = [];
    k = AnyKey;
    
    #key is fed AnyKey, root is a number
    def __init__(self, key, root):
        '''
        Constructor
        '''
        
        self.k = key;
        self.notes = key.c(root);
        
        if root < 8 and root > 0:
            self.root = root;
            if self.quality is None:
                self.quality = self.majorChords[root-1];
            #the plus is for augmented chords
            '''else:
                if quality == 'M' or quality == 'm' or quality == 'd' or quality == '+':
                    self.quality = quality;
                else:
                    print("Error, not a valid quality! (M, m, d, +)");
            '''
        else:
            print("Error, not a valid root!");