import speech_recognition as sr
import wolframalpha as wa
import pyttsx3
import random

# Voice A.I

r = sr.Recognizer()

hello = ["hi", "hey", "hey there", "hello"]

def say(data):
    engine = pyttsx3.init()
    engine.say(data)
    engine.runAndWait()


while True:

    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            if "karen":
                try:
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                        text = r.recognize_google(audio)
                        text = text.lower()
                        if "hello" or "hi" or "hey" in text:
                            say(random.choice(hello))
                        elif "your" in text:
                            say("This isn't about me, it's about you")
                        elif "who" and "you" in text:
                            say("I was created by Patrick Clark using many python library's including, speech recognition, text to speech, tkinter and man more")
                        else:
                            try:
                                client = wa.Client("LV36UH-GY4A2RV9WW")
                                res = client.query(text)
                                say(next(res.results).text)
                            except:
                                say("Sorry I don't know " + text)
                except:
                    say("Sorry I didn't catch that")
            else:
                pass
    except:
        pass
