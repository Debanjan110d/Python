a = "{0} is a fucking bitch {1}".format("Swarupa","girl")
print(a)

# importing the pyttsx library 
import pyttsx3 
  
# initialisation 
engine = pyttsx3.init() 
  
# testing 
engine.say(a) 
engine.say("I will kick her ass")
engine.runAndWait() 