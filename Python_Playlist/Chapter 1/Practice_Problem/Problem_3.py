# 3. Install an external module and use it to perform an operation of your interest. 
import pyttsx3
print("We install pttsx3 that convert text into speech")
engine = pyttsx3.init()

engine.say("Hey I am good")
engine.runAndWait()