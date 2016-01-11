from AnyKey import AnyKey #@UnresolvedImport
from Progression import Progression #@UnresolvedImport
from Voice import Voice #@UnresolvedImport

    
#Global vars
WELCOME = "\tWelcome to the Chorale Generator!"
TEMPO = 60;
def run():
    
    body = "";
    body += "(tempo! " + str(TEMPO) + ")\n"
    print(body);
    
    k = AnyKey("C M");
    p = Progression(k, 10);
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
        body += k.translate(v.voices[num-1]);
        
        #for note in v.voices[num-1]:
        #    body += " " + str(note);
        body += "\n";
    
    #body += "v1:" + str(v.soprano) + str(v.alto) + str(v.tenor) + str(v.bass);
    print(body);
    file.write(body);

def debug():
    k = AnyKey("C M");
    p = Progression(k, [1,5,4,6,1]);
    v = Voice(k, p);
    
    for voice in v.voices:
        voice
    

if __name__ == '__main__':
    run();
    #debug();