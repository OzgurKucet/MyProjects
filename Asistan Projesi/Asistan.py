# -*- coding: utf-8 -*-
import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from playsound import playsound
from gtts import gTTS
import os
import random
import feedparser
import datetime;


selamlama = ["nasılsın","iyi misin","Merhaba","İyi günler","Selam Nasıl gidiyor","Selam ne var ne yok","mutlu günler","Alo"]
selamlamaDonus = ["Merhaba","Hoşgeldin","nasıl yardımcı olabilirim","mutlu günler","esenlikler dilerim","selam nasıl gidiyor","selam ne var ne yok","Çok Yorgunum çünkü geliştiricilerim bana tüm gün boyunca yeni şeyler öğretiyor"]
tempature = ["derece","hava","kaç","hava kaç","sıcaklık kaç","sıcaklık","hava durumu"]
saat = ["saat","kaç","saat kaç","kaç saat","zaman"]
gun = ["bugün ayın kaçı","ayın","kaçı","bugün günlerden ne","günler","günlerden","bu gün ayın","tarih"]

r = sr.Recognizer()


def record(ask = False):
    if ask:
        speak(ask)
    with sr.Microphone() as source:
        audio = r.listen(source,phrase_time_limit=3)
        voice = ''
        try:
            voice = r.recognize_google(audio,language='tr-TR')
        except sr.UnknownValueError:
            speak("anlayamadım")
        except sr.RequestError:
            speak("sistem calismiyor")

    return voice

def response(voice):
    if voice in selamlama:
        if(voice == "iyi misin"):
            speak("iyiyim şikayetim yok")
        else:
            speak(str(selamlamaDonus[random.randint(0,len(selamlamaDonus)-1)]))

    if "arama yap"in voice:
        search = record("ne aramak istiyorsun")
        url = 'https://www.google.com/search?q=+'+search
        webbrowser.get().open(url)
        speak(search+ "için bulduklarım")
    if "tamamdır" in voice:
        speak("gorüşürüz")
        exit()
    if voice in tempature:
        speak("hava durumu şu şekilde")
        hava()
    if voice in saat:
        Saat()
    if voice in gun:
        tarih()

def speak(string):
    tts=gTTS(string,lang='tr')
    rand = random.randint(1,100000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)


def hava():
    parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|317049|kusadasi|")
    parse = parse["entries"][0]["summary"]
    parse = parse.split()
    print (parse[0],parse[2], parse[4], parse[5])
    hava2()

def hava2():
    parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|317049|kusadasi|")
    parse = parse["entries"][2]["summary"]
    parse = parse.split()
    print ("Tomorrow:",parse[0],parse[1],parse[2],parse[3],parse[4])
    return ("yarın:",hava2)

def tarih():
    gun 	  = datetime.datetime.now().strftime("%d");
    ay 	      = datetime.datetime.now().strftime("%m");
    yil 	  = datetime.datetime.now().strftime("%Y");
    tarihsaat = datetime.datetime.now().strftime("%d-%m-%Y");

    print ("Tarih : " ,tarihsaat);



def Saat():
    saat 	  = datetime.datetime.now().strftime("%H");
    dakika	  = datetime.datetime.now().strftime("%M");
    print ("Saat:" ,saat+":"+dakika);

speak("nasil yardimci olabilirim")
print("nasil yardimci olabilirim")
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)
