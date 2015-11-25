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
    legend = {'c': 0, 'd': 2, 'e': 4, 'f': -1, 'g': 1, 'a': 3, 'b': 5};
    notenames = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];
    notes = [];
    
    def __init__(self, key):
        '''
        Creates the notes array
        '''
        isValid = True;
        
        key = key[0].lower() + key[1:];
        print (key);
        
        if len(key) < 4 and len(key) > 1:
            #get index of where the KEY's note is.
            index = -1;
            for i in range(0, 7): #over each note in an octave
                if (key[0] == self.notenames[i]):
                    index = i;
            if index == -1:
                isValid = False;
                
            print("index is:" , index);
            
            if (key[len(key)-1] == 'M'):
                print("helloworld");
                SF = self.legend[key[0]]; #the number of sharps or flats
                for i in range(index, index + 7):
                    #if (key[])
                    print (i%7);
            elif (key[len(key)-1] == 'm'):
                print("howareyou");
            
            else:
                print("set at 1.5");
                isValid = False;
            if len(key) == 3:
                print("Len is 3");
        else:
            print("set at second");
            isValid = False;
        if isValid == False:
            print("Not a valid key!");
            
    def n(self, index):
        return self.notes[index -1];

if __name__ == '__main__':
    a = SuperKey("CbM");
    b = SuperKey("bm");