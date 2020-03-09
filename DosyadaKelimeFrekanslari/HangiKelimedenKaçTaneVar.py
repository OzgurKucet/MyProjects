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

def f(dosyaismi):
    with open(dosyaismi,"r") as dosya:
        tumKelimeler = []
        icerik = dosya.read()
        kelimeler = icerik.split()

        for kelime in kelimeler:
            tumKelimeler.append(kelime)
        tumKelimeler = sembolleriTemizle(tumKelimeler)
    return  tumKelimeler


tumKelimeler = []

for i in range(1,11):
    dosyaismi = str(i)+".txt"
    tumKelimeler += f(dosyaismi)


kelimesayisi = sozlukolustur(tumKelimeler)


for anahtar,deger in sorted(kelimesayisi.items(),key = operator.itemgetter(1)):
    print(anahtar,deger)

