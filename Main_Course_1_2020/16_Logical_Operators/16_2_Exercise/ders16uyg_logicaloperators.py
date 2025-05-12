### 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

#sayi=int(input("Sayi giriniz: "))
#result = 0<sayi and sayi<100
#print(result)

### 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
#sayi = int(input("Sayi giriniz: "))
#result = sayi%2==0 and sayi>0 
#print(f"Seçtiğiniz sayi çift ve pozitif mi? {result}")

### 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

#email = "kemalf1@hotmail.com"
#şifre = "kd12"
#girilenemail = input("Email adresinizi girin: ")
#girilenşifre = input("Şifrenizi girin: ")
#result=(email==girilenemail) and (girilenşifre==şifre)
#print(f"Girdiğiniz e-mail ve şifre {result}")


### 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız. 

#s1=int(input("1. sayiyi giriniz: "))
#s2=int(input("2. sayiyi giriniz: "))
#s3=int(input("3. sayiyi giriniz: "))

#result1vs2=s1>s2
#result1vs3=s1>s3
#result2vs3=s2>s3

#print(f"1. sayi 2. sayidan büyük mü? {result1vs2}")
#print(f"1. sayi 3. sayidan büyük mü? {result1vs3}")
#print(f"2. sayi 3. sayidan büyük mü? {result2vs3}")



### 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
       #Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırınız.
       # a) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
       # b) Finalden 70 alındığında ortalamanın önemi olmasın.

#vize1=int(input("1. vize notunuzu giriniz: "))
#vize2=int(input("2. vize notunuzu giriniz: "))
#final=int(input("Final notunuzu giriniz: "))

#ortalama= (((vize1+vize2)/2)*0.6) + (final*0.4)
#a result=ortalama>=50 and final>=50
#b result=ortalama>=50 or final>=70
#print(f"Ortalamanız: {ortalama} , dersten geçme durumunuz: {result}")


### 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
       # Formül: (Kilo / boy uzunluğunun karesi)
       # Aşağıdaki tabloya göre kişi hangi gruba girer?
       # 0    - 18.4 => Zayıf
       # 18.5 - 24.9 => Normal
       # 25.0 - 29.9 => Fazla kilolu
       # 30.0 - 34.9 => Şişman (Obez)

ad=input("Adınızı ve soyadınızı girin: ")
kilo=float(input("Kilonuzu kg biçiminde girin: "))
boy=float(input("Boyunuzu metre biçiminde girin: "))
vk = kilo/(boy**2)
vk=round(vk,1)
zayif =           0 < vk < 18.4
normal =       18.5 < vk < 24.9
fazlakilolu = 25.0 < vk < 29.9
obez =       30.0 < vk < 40.0
aşırıobez = 40 < vk 

print(f"{ad} adlı kişinin vücut kitle indeksi {vk} ve vücut durumu zayıf mı? {zayif} ")
print(f"{ad} adlı kişinin vücut kitle indeksi {vk} ve vücut durumu normal mi? {normal} ")
print(f"{ad} adlı kişinin vücut kitle indeksi {vk} ve vücut durumu fazla kilolu mu? {fazlakilolu} ")
print(f"{ad} adlı kişinin vücut kitle indeksi {vk} ve vücut durumu obez mi? {obez} ")
print(f"{ad} adlı kişinin vücut kitle indeksi {vk} ve vücut durumu aşırı obez mi? {aşırıobez} ")


