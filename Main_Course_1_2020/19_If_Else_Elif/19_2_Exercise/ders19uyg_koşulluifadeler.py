# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip 
# ehliyet alabilme durumunu kontrol ediniz. 
# Ehliyet alma koşulu için
# en az 18 yaşında ve eğitim durumu lise ya da 
# üniversite olmalıdır.

#ad=input("Ehliyet alma durumunu sorgulamak istediğiniz kişinin adını ve soyadını girin: ")
#yaş=int(input("Kişinin yaşını girin: "))
#eğitim=input("Kişinin eğitim durumunu girin: ")
#if (yaş >= 18):
#    if (eğitim=="lise" or eğitim=="üniversite"):
#        print(f"{ad} ehliyet almak için uygun.")
#    else:
#        print(f"{ad}'nin ehliyet almaya yaşı uygun ancak ehliyet alabilmek için lise veya üniversite mezunu olması gerekiyor.")
#else: 
#    print(f"{ad}'in yaşı yetmediğinden ehliyet alamaz.")



# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan
# ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
# 0-24   => 0
# 25-44  => 1
# 45-54  => 2
# 55-69  => 3
# 70-84  => 4
# 85-100 => 5

#ad=input("Öğrencinin adı ve soyadı:")
#y1=int(input("Öğrencinin 1. yazılı notunu girin: "))
#y2=int(input("Öğrencinin 2. yazılı notunu girin: "))
#s=int(input("Öğrencinin sözlü notunu girin: "))
#ort=(y1+y2+s)/3
#print(f"Öğrencinin ortalaması: {ort}")
#if(0<ort and ort<24):
#    print(f"{ad} adlı öğrencinin not puanı: 0. Berbatsın.")
#elif(25<ort<44):
#    print(f"{ad} adlı öğrencinin not puanı: 1. Çalışmıyorsun.")
#elif(45<ort<54):
#    print(f"{ad} adlı öğrencinin not puanı: 2. Az çalışıyorsun, çabala.")
#elif(55<ort<69):
#    print(f"{ad} adlı öğrencinin not puanı: 3. Sende ışık var, daha çok çalışırsan başaracaksın.")
#elif(70<ort<84):
#    print(f"{ad} adlı öğrencinin not puanı: 4. İyi gidiyorsun.")
#elif(85<ort<100):
#    print(f"{ad} adlı öğrencinin not puanı: 5. Tebrikler!")
#else:
#    print("Geçersiz değer girdiniz, lütfen tekrar deneyin.")





# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını
# aşağıdaki bilgilere göre hesaplayınız
# 1. Bakım => 1. yıl
# 2. Bakım => 2. yıl
# 3. Bakım => 3. yıl
# Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı
# olarak hesaplayınız. Datetime modülü kullanılmalı.
# (simdi) - (2018/8/1) => kalan gün

import datetime
tarih = input("Aracınız hangi tarihte trafiğe çıktı?(2019/8/9 formatında yazın) ")
tarih = tarih.split("/")

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days


if days<=365:
    print(f"Aracınız trafiğe çıkalı {days} gün geçmiş. 1. servis aralığındasınız.")
elif 365<days and days<365*2:
    print(f"Aracınız trafiğe çıkalı {days} gün geçmiş. 2. servis aralığındasınız.")
elif 365*2<days and days<365*3:
    print(f"Aracınız trafiğe çıkalı {days} gün geçmiş. 3. servis aralığındasınız.")
else:
    print("Hatalı süre bilgisi girdiniz.")
