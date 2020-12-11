# -*- coding: utf-8 -*-
import speech_recognition as sr
from gtts import gTTS
import os
import time
from os import system as komut


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='tr')
    tts.save("audio2.mp3")
    os.system("audio2.mp3")


with open("deneme.txt","r",encoding='utf8') as dosya:#ortaya biryere eklemek...
    data = dosya.read()
    speak(data)

