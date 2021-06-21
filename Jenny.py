import pyttsx3,datetime,wikipedia,webbrowser,os
import speech_recognition as sr
from selenium import webdriver
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    print("Jenny:"+audio.upper())
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>12 and hour<17:
        speak("good afternoon!")
    else:
        speak("good evening")
    speak("I am Jenny, how can I help you?")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language="en-in")
        print("You:"+query.upper())
    except :
        speak("pardon me sir!! say that again plese")
        return "None"
    return query
def main():
    wishme()
    while True:
        query=takecommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia"+results)
        elif "my name" in query:
            speak("You are shivendra. You are in B tech first year.")
        elif "love you" in query or "marry me" in query:
            speak("I am a robot, how can i marry you sir? if you want i can find a bride for you")
        elif "Hello" in query:
            speak("Hello sir, how are you?")
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "google" in query:
            query=query.replace("search google for","")
            webbrowser.open("https://www.google.com/search?q="+query)
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open geeks for geeks" in query:
            webbrowser.open("geeksforgeeks.com")
        elif "open codechef" in query:
            webbrowser.open("codechef.com")
        elif "open codeforces" in query:
            webbrowser.open("codeforces.com")
        elif "play music" in query or "open spotify" in query:
            os.system("spotify")
        elif "open powerpoint" in query:
            os.system("powerpoint")
        elif "open word" in query:
            os.system("winword")
        elif "open excel" in query:
            os.system("excel")
        elif "time" in query:
            timestr=datetime.datetime.now().strftime("%H:%M")
            speak("Sir the time is "+timestr)
        elif "your name" in query:
            speak("Hi, myself Jenny")
        elif "about yourself" in query or "you can do" in query:
            speak("Myself Jenny,I can perform certain simple tasks like browsing and telling time. calculation is yet to be developed. my owner is Shivendra. I am developed in python")
        elif "stop" in query:
            speak("Bye sir, have a nice day")
            exit()
       
       
        
main()
