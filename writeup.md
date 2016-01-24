# Chorale Generator Write-up

This code explanation is intended for non-programmers, so I think a few programming basics should be elucidated before I proceed with an in-depth explanation of the Chorale Generator.

1. **Variables** - just like in math, except we can assign text, true/false (boolean) values, and other cool stuff to them as well.

2. **Loops** - they come in two main variants: for and while. One reason I chose to write my program in the Python programming language is that one can often get away with reading the source code like English. A for loop is read like “for every ____ in ____, do ____.” A while loop is read like “while ____ is true, do ____.” These constructs allow the programmer to automate certain tasks, like adding 1 to every element in an array.

3. **Functions/methods** - again, kind of like math, but not really. They can also run code, in addition to changing their inputs. If the function returns a number, string, etc. the programmer can treat the function like that data structure.

4. **Classes/objects** - All files except for main.py are classes. They define a certain type (or class) of objects. You can write an apple class, which will encompass all apples. It will include attributes like weight and color. The class will also have functions (verbs) such as beEaten, rot, or doNothing. An object is a specific instance of that class. Doing things to that object will not affect all apples, just that one, specific apple.

5. **Comments** - in Python, they are usually denoted by a # symbol. They can also be any text in between three apostrophes or quotation marks. They are ignored by the program, added for whoever reads the code.

#### Installation
You will need the following to run Chorale Generator:
+ python3
+ the Java 8 Runtime Environment
+ alda (programming language)

Execute `python3 main.py` in the same directory my source code is installed. 

Note: Sometimes, the option to play the alda code doesn't work, so it may be best to start the alda environment from another shell. To do this, navigate to your file's directory and execute `alda play --file FILENAME`.
***
#### Overview
From a high-level perspective, this program has five main stages:
1. Get user input
2. Initialize the AnyKey class
3. Generate a chord progression
4. Generate voices
5. Write the result to a file
***
#### main.py
This class is the wrapper for the dirty work. It contains the user interface and generates usable Alda code from the generated voices.

First, the program imports the `AnyKey`, `Progression`, `Voice`, and `system` classes. `system` is used to play the file without the user having to open up another shell session:
```python
from AnyKey import AnyKey #@UnresolvedImport
from Progression import Progression #@UnresolvedImport
from Voice import Voice #@UnresolvedImport
from os import system
```

`getInput()` and `getNum()` are helper functions that provide rudimentary error-checking for user input:
```python
def getInput(message):
#CODE REMOVED

def getNum(message):
#CODE REMOVED
```

Execution actually starts at the bottom of the file:
```python
if __name__ == '__main__':
    run();
    #debug();
```
The if statement calls the `run()` function if main.py is being run as a standalone program.

The `run()` function first asks the user to define several variables the program will need to begin generating music: tempo, filname, key, and the number of measures. After that, it instantiates the `AnyKey`, `Progression`, and `Voice` classes:
```python
    k = AnyKey(KEY_SIGNATURE);
    p = Progression(k, NUMBER_OF_NOTES);
    v = Voice(k, p);
```
`run()` then extracts the correct notes for each voice, then writes everything to a file in correct Alda syntax:
```
    file = open(FILENAME, 'w');
    body += "piano:\n";
    
    for num in range(0, len(v.voices)):
        body += "V" + str(num+1) + ": o" +str(num+1);
        body += " " + k.translate(v.voices[num-1])
        body += "\n";
```
The line directly under the `for` loop splits up each voice into its respective octave (bass = lowest octave, tenor = second lowest octave, etc.)

Finally, `main.py` asks the user if he or she wants to play the generated score. I've had mixed success with playing it from the program, though, so it may be best to navigate to Chorale Generator's directory and play the file from another shell.
***
#### AnyKey.py
This is a class is intended to interface between the rest of the program and a specific key. It's main purpose is to translate scale degrees (in numerical form) into actual notes within a certain key.

The entire `__init__()` function's main purpose is to get the correct letter names of each note in the key.

The following code adds the correct alterations to each note, depending on the key signature (for example, the key of A major will have a sharpened f, c, and g).
```python
    legend = {'c': 0, 'd': 2, 'e': 4, 'f': -1, 'g': 1, 'a': 3, 'b': 5};
    #INTERMEDIARY CODE REMOVED
            KS = 0;
            #INTERMEDIARY CODE REMOVED
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
```
Other code in the function fills out the `chords` and `notes` arrays. I thought wasn't sure if I'd need them (they were redundant because I had `chordNotes`), but decided to implement them just in case.

I have two accessor methods to get the letter(s) of notes and chords in the key. I did not end up using this functionality in the final code, however, the methods were extremely useful during the early stages of planning and debugging. The last (and most useful function) is `translate()`, which takes an array of numbers and returns their letter name in the key.
***
#### Chord.py
In the interest of extensibility, I added a lot of stuff that isn't strictly needed. In the `Progression` class, the chord progression is actually a list of `Chord` objects.

Thus, wrote this chord class in case I decided to add the ability to generate secondary dominants or non-key tones in the chorale. This class is mostly self-explanatory. When the chord object is initialized, it checks to see if it has a valid root numeral (later, I plan to change this to an actual letter note):
```python
 if root < 8 and root > 0:
            self.root = root;
```
then it will always default to the chord quality in major, given by `majorChords = ['M', 'm', 'm', 'M', 'M', 'm', 'd'];`.
***
#### Progression.py
Here, we get get into the meat of the program. The class uses a Markov chain to transition between "tiers" of chords:
```python
    first = [1];
    second = [5, 7];
    third = [4, 3];
    fourth = [6,2];
```

createProgression() first seeds the random number generator:
```python
        seed = datetime.datetime.now();
        random.seed(str(seed));
```
`chain` is a dictionary that correlates each chord in the key with a list that contains tiers of chords. The program chooses a random chord from the list that corresponds with the last chord in the progression. `chain` contains some redundancies in order to increase the chances of a certain tier being called. 
***
#### Voice.py
The `__init__()` function of this class takes care of everything. Originally, the purpose of the voice class was to model one voice. This way, the program could have a variable number of voices. However, as I worked more on the program, I decided to have the Voice class just generate all four voices. This would eliminate the need to have each `Voice` object communicate with the other to figure out voicing issues.

The following code calls the `createVoice()` function for every voice. The `NUMBER_OF_VOICES` variable is hardcoded as 4.
```python
for num in range(0, self.NUMBER_OF_VOICES):
    self.voices.append(self.createVoice());
```
The `createVoice()` function chooses a random note from the available ones for each chord in the progression. Each spot in the array is equal to a quarter note.

Finally, the `__init__()` function goes back and edits the voicing for the first and last two chords. The voicing of all three chords is changed to root position with a doubled root in the soprano. The first and last chords are turned to I chords, and the second-to-last chord is turned to a V.
