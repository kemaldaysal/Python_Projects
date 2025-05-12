def not_hesapla(satir):
    satir = satir[:-1] # farklı öğrencilerin notlarının arasındaki boşluklar alındı.
    liste = satir.split(':')
    
    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = float(notlar[0])
    not2 = float(notlar[1])
    not3 = float(notlar[2])

    ortalama = (not1+not2+not3)/3

    if ortalama>=90 and ortalama<=100:
        harf = "AA"
    elif ortalama>=80 and ortalama<=89.9:
        harf = "BA"    
    elif ortalama>=70 and ortalama<=79.9:
        harf = "BB"
    elif ortalama>=65 and ortalama<=69.9:
        harf = "CB"
    elif ortalama>=60 and ortalama<=64.9:
        harf = "CC"
    elif ortalama>=50 and ortalama<=59.9:
        harf = "DD"
    elif ortalama>=30 and ortalama<=49.9:
        harf = "FD"
    else:
        harf = "FF"

    return ogrenciAdi + ": " + harf + "\n"


def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="UTF-8") as file:
        for satir in file:
            print(not_hesapla(satir))


def not_gir():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    not1 = input("Not 1: ")
    not2 = input("Not 2: ")
    not3 = input("Not 3: ")

    with open("sinav_notlari.txt","a",encoding="UTF-8") as file:
        file.write(f"{ad} {soyad}:{not1},{not2},{not3}\n")

def notlari_kaydet():
    with open("sinav_notlari.txt","r",encoding="UTF-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt","w",encoding="UTF-8") as file2:
            for i in liste:
                file2.write(i)

while True:
    islem = input("1- Notları oku\n2- Not gir\n3- Notları kaydet\n4- Çıkış\n")

    if islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kaydet()
    else:
        break
