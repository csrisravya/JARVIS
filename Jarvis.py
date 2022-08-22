from datetime import datetime
import pyttsx3 # Test to speech conversion
import speechRecognition as sr

engine  = pyttsx3.init('sapi5') # Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis . It provides male and female voices
                                # Using sapi5 , we are able to use the inbuilt voice provided by windows
voices = engine.getProperty('voices') # getting the voices
# print(voices) : prints all the voices the system can provide us.
engine.setProperty('voice',voices[1].id) # to set the voice
                                          # 0 is the voice of david(man). 1 is the voice of zira
def speak(audio):
    engine.say(audio) 
    engine.runAndWait() # This function will make the speech audible in the system. The speech will not be audible if this command isnt written

def greeting() : 
    hour = int(datetime.now().hour) # datetime is a module which hepls work with date and time 
                                            # hours here gives teh hour on the clock in int type.
    if hour>=0 and hour<12 : 
        speak("Good morning dear user ") 
    elif hour>= 12 and hour<18:
        speak("Good Afternoon dear user.")
    else:
        speak("Good Evening dear user . It is presently")
    speak("This is Jarvis. How may I help you ?")
if __name__ == "__main__" : 
    # speak(" Hello , This is Jarvis ")
    greeting()
