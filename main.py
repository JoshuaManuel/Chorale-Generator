from AnyKey import AnyKey #@UnresolvedImport
from Progression import Progression #@UnresolvedImport
from Voice import Voice #@UnresolvedImport
from Chord import Chord #@UnresolvedImport

    
#Global vars

TEMPO = 80;
def run():
    body = "";
    body += "(tempo! " + str(TEMPO) + ")\n"
    print(body);
    
    
    k = AnyKey("F#M");
    p = Progression(k, [1,5,4,6,1]);
    v = Voice(k, p);
    
    file = open('test.alda', 'w');
    
    body += "piano:\n";
    
    '''
    for num in range(0, len(p.prog)):
        #print(num)
        body += " " + p.prog[num].notes;
    
    print(body);
    #file.write(body);
    '''
    
    for num in range(1, len(v.voices)+1):
        body += "V" + str(num) + ": o" +str(num);
        for note in v.voices[num-1]:
            body += " " + note;
        body += "\n";
    
    #body += "v1:" + str(v.soprano) + str(v.alto) + str(v.tenor) + str(v.bass);
    print(body);
    file.write(body);

if __name__ == '__main__':
    run();