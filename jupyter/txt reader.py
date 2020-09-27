import pyttsx3 as pts

in_file='book.txt'

engine=pts.init()

with open(in_file,'r') as f:
    for eachline in f:
        engine.say(eachline)
        engine.runAndWait()
