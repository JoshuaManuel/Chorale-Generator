from AnyKey import AnyKey #@UnresolvedImport
from Progression import Progression #@UnresolvedImport
from Voice import Voice #@UnresolvedImport
from subprocess import call
from os import system;
    
#Global vars
WELCOME = '''
\t Welcome to Joshua's chorale                   
  ____                           _             
 / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_| |  __/ | | |  __/ | | (_| | || (_) | |   
 \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                               
'''
TEMPO = 60;

def getInput(message):
    varSet = False;
    ans = "";
    while(not varSet):
        try:
            ans = input(message);
            varSet = True;
        except:
            print("Invalid input!");
    return ans;

def getNum(message):
    varSet = False;
    ans = 0;
    while(not varSet):
        try:
            ans = int(input(message));
            varSet = True;
        except:
            print("Invalid input! Enter a number!");
    return ans;
    
def run():
    
    print(WELCOME);
    TEMPO = getNum("How many beats per minute? (60-100 recommended)\n");
    NUMBER_OF_MEASURES = getNum("How many measures do you want?\n");
    KEY_SIGNATURE = getInput("What key? (ex. AbM, C M, F#M)\n");
    FILENAME = getInput("What do you want to call the swag piece?\n");
    FILENAME += ".alda";
    NUMBER_OF_NOTES = NUMBER_OF_MEASURES*4-2
    
    print("Inputs: " + str(TEMPO) + " " + KEY_SIGNATURE);

    body = "";
    body += "(tempo! " + str(TEMPO) + ")\n"
    
    k = AnyKey(KEY_SIGNATURE);
    p = Progression(k, NUMBER_OF_NOTES);
    v = Voice(k, p);
    
    
    file = open(FILENAME, 'w');
    
    body += "piano:\n";
    
    for num in range(0, len(v.voices)):
        body += "V" + str(num+1) + ": o" +str(num+1);
        body += " " + k.translate(v.voices[num-1])
        body += "\n";
    
    #body += "v1:" + str(v.soprano) + str(v.alto) + str(v.tenor) + str(v.bass);
    print(body);
    file.write(body);
    system("pwd");
    shouldPlay = input("Do you want to play your piece? (y/n)\nIt may take a while to start up...\n");
    
    if shouldPlay.lower() == 'y':
        system("alda play --file " + FILENAME);
        
    

def debug():
    k = AnyKey("C M");
    p = Progression(k, 10-2);
    v = Voice(k, p);
    
    for voice in v.voices:
        voice
    

if __name__ == '__main__':
    run();
    #debug();