
from datetime import datetime
import pyttsx3 # Test to speech conversion
import speech_recognition as sr
import webbrowser # module offers a high-level interface that enables showing the documents based on the web


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
    
def takeCommand():
    # Takes microphone input from user and returns string output
    r = sr.Recognizer() # Recognizer helps us recognize audio
    with sr.Microphone() as source:
        print("Listening.....")
        # press on the method along with ctrl to access the documentation of the method
        r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
            

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')  #  Performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using the Google Speech Recognition API.
        print(f"You said : {query}\n")
    
    except Exception as e:
        print(e)
        print("Could not understand. Please try again.")
        return "none"  # returns none string in case there is an error
    return query
    
    
        
    
    
if __name__ == "__main__" : 
    # speak(" Hello , This is Jarvis ")
    greeting()
     # takeCommand()
    while True:
        query = takeCommand().lower() # we are converting our speech command to string and storing it in query 
        if "open google" in query:
            webbrowser.open("google.com")
        elif "open youtube" in query:
            webbrowser.open_new_tab("youtube.com")
            
