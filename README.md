# JARVIS-PRIVATE-

pyttsx3 
pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3. An application invokes the pyttsx3.init() factory function to get a reference to a pyttsx3. 
The pyttsx3 module supports two voices first is female and the second is male which is provided by “sapi5” for windows. It supports three TTS engines :
sapi5 – SAPI5 on Windows
nsss – NSSpeechSynthesizer on Mac OS X
espeak – eSpeak on every other platform

speech_recognition
Library for performing speech recognition, with support for several engines and APIs, online and offline.
Speech recognition engine/API support:
CMU Sphinx (works offline)
Google Speech Recognition
Google Cloud Speech API
Wit.ai
Microsoft Bing Voice Recognition
Houndify API
IBM Speech to Text
Snowboy Hotword Detection (works offline)


Google Recognizer function uses Google’s free web search API. We have used the Google Recognizer function, which is recognize_google(). It’s free and doesn’t require an API key to use. There is one drawback about this recognizer, it limits you when you want to work with longer audio files.



Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
Search Wikipedia, get article summaries, get data like links and images from a page, and more. Wikipedia wraps the MediaWiki API so you can focus on using Wikipedia data, not getting it.
We need to install the module and we can do so by typing "pip install wikipedia" in your terminal

import smtplib:
Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and routing e-mail between mail servers.

Python provides smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.Is Smtplib inbuilt in Python?
Python comes with the built-in smtplib module for sending emails using the Simple Mail Transfer Protocol (SMTP). smtplib uses the RFC 821 protocol for SMTP.
For sending the email we need to enable less secure apps in our gmail. Google has now disabled this feature. Hence we need to enable it but genrating a special password. To generate the password use the following steps:
1. Open ur gamil
2. Go to your account
3. Click on manage your google account
4. Click on security
5. Turn on 2 step verification under the Signing in to Google box
6. Click on App passwords and select the needed and then generate the password
