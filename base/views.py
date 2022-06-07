from django.shortcuts import render
from django.http import HttpResponse
import gtts 
import os
from playsound import playsound
import speech_recognition as sr
import pyttsx3

def index(request):
    return render(request, 'index.html')

def tts(request):
    if request.method=="POST":
        text=request.POST.get("tts")
        print(text)
        t1 = gtts.gTTS(text=text, slow=False) 
        t1.save("t2s.mp3")
        t1.save("t2s.wav")
        playsound("t2s.mp3")
        os.remove("t2s.mp3")
    return render(request, 'tts.html')

def stt(request):
    r = sr.Recognizer()
    def SpeakText(command):
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
    while(1):
        try:
            print("Speak")
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print(MyText)
                SpeakText(MyText)
                break
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occured")
    return render(request,"stt.html",{"text": MyText})
