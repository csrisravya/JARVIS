from asyncio import exceptions
import pyjokes
import wikipedia #Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
from datetime import datetime
import pyttsx3 # Test to speech conversion
import speech_recognition as sr #Library for performing speech recognition with the Google Speech Recognition API.
import webbrowser # module offers a high-level interface that enables showing the documents based on the web. To browse the web and open any webpage
import smtplib #The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.

engine  = pyttsx3.init('sapi5') # Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis . It provides male and female voices
                                # Using sapi5 , we are able to use the inbuilt voice provided by windows
voices = engine.getProperty('voices') # getting the voices
# print(voices) : prints all the voices the system can provide us.
engine.setProperty('voice',voices[1].id) # to set the voice
                                          # 0 is the voice of david(man). 1 is the voice of zira
#The first and foremost thing for an A.I. assistant is that it should be able to speak. To make our J.A.R.V.I.S. talk, we will make a function called speak(). This function will take audio as an argument, and then it will pronounce it.
#Now, the next thing we need is audio. We must supply audio so that we can pronounce it using the speak() function we made. We are going to install a module called pyttsx3.
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
    #take command with the help of the microphone of the user's system. So, now we will make a takeCommand() function.  With the help of the takeCommand() function, our A.I. assistant will return a string output by taking microphone input from the user.
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


#SMTP: Simple Mail Transfer Protocol    
def sendGmail(to,message): # we do this using smtplib which is a python package used to send email via gmail
                          #but we need to allow the less secure apps for smtplib to allow us to ssnd an email
                          #enable less secure apps to all users.  Since google has dissabled the feature. We need to generate the password for third party access. Check out the readme file to know how to generate the password
    server = smtplib.SMTP("smtp.gmail.com,587")   #port number 587. This line creates our SMTP server session
    server.ehlo() #Hostname to identify itself
    server.starttls()  # puts the connection to the SMTP server into TLS mode. TLS stands for transfer layer security. It is for connecting purpose. TLS is used to add security 
    server.login("sender_email@gmail.com","password_of_the_sender_gmail") #here password_of_the_sender_gmail is the passowrd which u generate
    server.sendmail('sender_email@gmail.com',to,message)
    server.close()
    
if __name__ == "__main__" : 
    # speak(" Hello , This is Jarvis ")
    greeting()
     # takeCommand() 
      #Logic for executing tasks based on query
    while True:
        query = takeCommand().lower() # we are converting our speech command to string and storing it in query. #converting query to lower case
        if "open google" in query:
            webbrowser.open("google.com")
        elif "open youtube" in query:
            webbrowser.open_new_tab("youtube.com")
        elif 'send email' in query:
            try:
                speak("What would be the message?")
                content = takeCommand()
                to = "sender_email@gmail.com"
                sendGmail(to,"Hello,this is sent through python")
                speak("Your message has been sent via an email!")
            except Exception as e:
                print(e)
         elif 'wikipedia' in query: #if the word wikipedia is there in the command it will search wikipedia
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2) #Plain text summary of the page.
            speak('According to wikipedia')
            print(results)
            speak(results)
         elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")
         elif 'open website' in query:
            speak('Please type the name of the website you want to visit. Please specify the full url')
            website_name=input() #taking the name of the website as an input from the user
            print(website_name)
            webbrowser.open_new_tab(website_name)
        elif 'the time' in query:
            strTime=datetime.now().strftime("%H:%M:%S")  #strftime is string format time. The strftime() method takes one or more format codes as an argument and returns a formatted string based on it. 
            speak(f"Man, the time is {strTime}")
            print(f"The time is {strTime}")
        elif 'the date' in query:
            strDate=datetime.now().strftime("%D%M%Y")
            speak(f"Mam the date is {strDate}")
            print(f"The date is {strDate}")
        elif 'jokes' in query:
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)
    
            
                        
  
        
            
            
