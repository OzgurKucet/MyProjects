#!/usr/bin/python3
# -*- coding: utf-8 -*-

import operator
def sembolleriTemizle(tumKelimeler):
    sembolsuzkelimeler = []
    semboller = "!'@.^#<>+-_{}\",[]-=:;*/)(&"
    for kelime in tumKelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol,"")
        if(len(kelime)>0):
            sembolsuzkelimeler.append(kelime)
    return sembolsuzkelimeler

def sozlukolustur(tumKelimeler):
    kelimesayisi = {}

    for kelime in tumKelimeler:
        if kelime in kelimesayisi:
            kelimesayisi[kelime] += 1
        else:
            kelimesayisi[kelime] = 1

    return kelimesayisi

def sozlukKelimeninYanındakiKelimeler(tumKelimeler,kelime):
    liste = []
    for i in range(len(tumKelimeler)-1):
        if kelime == tumKelimeler[i]:
            liste.append(tumKelimeler[i+1])

    return liste

def sozlukKelimeninYanındakiKelimeler1(tumKelimeler,kelime):
    liste = kelime.split()
    liste2 = []

    for i in range(len(tumKelimeler)-1):
        for j in range(len(liste)):
            if tumKelimeler[i] == liste[j]:
                i+=1
                if(j == len(liste)-1):
                    liste2.append(tumKelimeler[i])
    return liste2

def f(dosyaismi):
    with open(dosyaismi,"r") as dosya:
        tumKelimeler = []
        icerik = dosya.read()
        kelimeler = icerik.split()

        for kelime in kelimeler:
            tumKelimeler.append(kelime)
        tumKelimeler = sembolleriTemizle(tumKelimeler)
    return  tumKelimeler

def inputtanoku(dosyaismi):
    with open(dosyaismi,"r") as dosya:
        cumleler = dosya.readlines()
        return  cumleler

def kelimeSayisiBestenBuyukMu(cumle):
    for kelimeler in cumle:
        for kelime in kelimeler:
            kelime = kelimeler.split()
            if(len(kelime)>5):
                return -1
    return 1

def sozlukteHangisininKelimeSayisiBuyuk(sozluk):
    enbuyuk = 0
    try:
        for kelime,value in sozluk.items():
            if(value>enbuyuk):
                enbuyuk = value
                EnÇokGecen = kelime
        return EnÇokGecen
    except UnboundLocalError:
        print("")

tumKelimeler = []



def EnÇokGeçenKelime(inputcumleler):
    dosyaOutput = open("output.txt","w")
    for kelimeler in inputcumleler:
            kelime = kelimeler.split()
            try:
                if len(kelime) == 1:
                    liste = sozlukKelimeninYanındakiKelimeler(tumKelimeler,kelime[0])
                    kelimesayisi = sozlukolustur(liste)
                    """for anahtar,deger in sorted(kelimesayisi.items(),key = operator.itemgetter(1)):
                        print(anahtar,deger)
                    """
                    enCokGecenKelime = sozlukteHangisininKelimeSayisiBuyuk(kelimesayisi)
                    #print(kelime[0],enCokGecenKelime)
                    dosyaOutput.write(kelime[0]+" "+enCokGecenKelime+"\n")


                elif len(kelime) == 2:
                    kelime = kelime[0] +" "+kelime[1]
                    liste = sozlukKelimeninYanındakiKelimeler1(tumKelimeler,kelime)
                    kelimesayisi = sozlukolustur(liste)

                    enCokGecenKelime = sozlukteHangisininKelimeSayisiBuyuk(kelimesayisi)
                    #print(kelime,enCokGecenKelime)
                    dosyaOutput.write(kelime+" "+enCokGecenKelime+"\n")

                elif len(kelime) == 3:
                    kelime = kelime[0] +" "+kelime[1]+" "+kelime[2]
                    liste = sozlukKelimeninYanındakiKelimeler1(tumKelimeler,kelime)
                    kelimesayisi = sozlukolustur(liste)

                    enCokGecenKelime = sozlukteHangisininKelimeSayisiBuyuk(kelimesayisi)
                    #print(kelime,enCokGecenKelime)
                    dosyaOutput.write(kelime+" "+enCokGecenKelime+"\n")
                elif len(kelime) == 4:
                    kelime = kelime[0] +" "+kelime[1]+" "+kelime[2]+" "+kelime[3]
                    liste = sozlukKelimeninYanındakiKelimeler1(tumKelimeler,kelime)
                    kelimesayisi = sozlukolustur(liste)

                    enCokGecenKelime = sozlukteHangisininKelimeSayisiBuyuk(kelimesayisi)
                    #print(kelime,enCokGecenKelime)
                    dosyaOutput.write(kelime+" "+enCokGecenKelime+"\n")

                elif len(kelime) == 5:
                    kelime = kelime[0] +" "+kelime[1]+" "+kelime[2]+" "+kelime[3]+" "+kelime[4]
                    liste = sozlukKelimeninYanındakiKelimeler1(tumKelimeler,kelime)
                    kelimesayisi = sozlukolustur(liste)

                    enCokGecenKelime = sozlukteHangisininKelimeSayisiBuyuk(kelimesayisi)
                    #print(kelime,enCokGecenKelime)
                    dosyaOutput.write(kelime+" "+enCokGecenKelime+"\n")
            except TypeError:
                dosyaOutput.write("-------Hatalı giriş yapmışsınız böyle bir kelime 10 txt dosyasında da geçmiyor!!!!!!!-------\n")


for i in range(1,11):
    dosyaismi = str(i)+".txt"
    tumKelimeler += f(dosyaismi)


kelimesayisi = sozlukolustur(tumKelimeler)

inputcumleler = inputtanoku("input.txt")

a = kelimeSayisiBestenBuyukMu(inputcumleler)

if a==-1:
    print("inputa girilen kelime sayisi 5 i gecemez...")
    exit(1)

EnÇokGeçenKelime(inputcumleler)

print("İnput Dosyasına Girdikleriniz Output Dosyasına Başarıyla Yazdirilmiştir...")
"""
for anahtar,deger in sorted(kelimesayisi.items(),key = operator.itemgetter(1)):
    print(anahtar,deger)
"""


