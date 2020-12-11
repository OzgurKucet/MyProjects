# -*- coding: utf-8 -*-
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from gtts import gTTS
import os
import time
from os import system as komut
# Record Audio

dosyaismi = input("Lütfen sese çevrilecek kelimelerin yazılacağı dosya ismini girin")
dosyaismi += ".txt"


while(True):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    flag = False
    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = r.recognize_google(audio,language="tr")
        print("You said: " + text)
        flag = True
        text = text.lower()
        print("text :",text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    with open(dosyaismi, "a",encoding="utf-8") as dosya:
        if text == "çıkış":
            exit()
        else:
            dosya.write(text)
            dosya.write("\n")

