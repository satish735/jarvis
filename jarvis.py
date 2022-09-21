!pip install pipwin 
!pip install pyttsx3
!pip install SpeechRecognition
!pipwin install webbrowser
!pip install wikipedia
!pipwin install os
!pip install smtplib
!pip install soundfile





import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import smtplib
import soundfile as sf







  engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

   
def wissMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour == 0 and hour<12 :
        speak("good morning sir")
    elif hour >=12 and hour<18:
        speak("good afternoon  sir ")
    else:
        speak("good evening sir ")
    speak(" I am jarvis. please tell me how  may  I help you ") 
    
def takeCommand():
    #it take microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print(" Listening...... ")
        r.pause_threshold = 1
        audio = r.listen(sourse)
        
    try:
        print("recognizing....")
        query = r.recognize_google(audio)
        print("user said : ", query )
         
        
    except Exception as e:
        print(e)
        
        print("say that again please....")
        
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('2021mcasatish10200@poornima.edu.in', 'Satish@12345')
    server.sendEmail('2021mcasatish10200@poornima.edu.in',to , contant)
    server.close()
    
    




if __name__ == "__main__":
    #wissMe()
    
    while True:
        query = takeCommand().lower() 
        
        if "wikipedia" in query:
            speak("serching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=3)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open canva" in query:
            webbrowser.open("https://www.canva.com/en_in/")
            
        elif "close program" in query:
            break
        elif "time" in query: 
            strftime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"hi sir time is {strftime}")
        elif "play music" in query:
            music = 'F:\\music'
            song = os.listdir(music)
            print(song)
            os.startfile(os.path.join(music ,  song[-1]))
                
        elif "mail" in query:
            try:
                speak('what should i say ')
                content = takeCommand()
                to = 'satish2021choudhary@gmail.com'
                sendEmail(to , content)
                speak('Email has been send ')
            except Exception as e:
                print(e)
                speak('sorry sir i am not able to send this mail')
                
           
        
        
print(sf.write('F:\\music\\my_Audio_file.mp3', speak))   
   
