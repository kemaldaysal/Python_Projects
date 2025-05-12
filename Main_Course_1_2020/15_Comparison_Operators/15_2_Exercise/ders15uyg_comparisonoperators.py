###1- Girilen 2 sayıdan hangisi büyüktür?

#a = int(input("a: "))
#b = int(input("b: "))
#result = (a > b)
#print(f"a({a}), b({b})'den büyüktür ifadesi doğru mu?3 {result} ")

###2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.

#vize1 = float(input("1. vize notunuzu girin: "))
#vize2 = float(input("2. vize notunuzu girin: "))
#final = float(input("Final notunuzu girin: "))
#ortalama=(((vize1+vize2)/2)*0.6)+(final*0.4)
#print(f"Ortalamanız:{ortalama} ve dersten geçme durumunuz: {ortalama>=50}")

###3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

#sayi = int(input("Bir sayı girin: "))
#tekcift = (sayi%2 == 0)
#print(f"Girdiğiniz {sayi} sayısı tek mi? {tekcift} ")

###4- Girilen bir sayının negatif pozitif durumunu öğrenin.
#sayi=int(input("Bir sayı giriniz: "))
#pozitifmi=(sayi > 0)
#print(f"Girilen sayinin pozitif olma durumu: {pozitifmi}")

###5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
# (email: email@sadikturan.com parola:abc123)

email="email@sadikturan.com"
password="abc123"

girilenemail=input("E-mail adresinizi girin: ")
girilenpassword=input("Parolanızı girin: ")

isEmail = (email == girilenemail.strip()) # Strip koyduğumuzdan doğru emailin sonuna boşluk koysak bile boşlukları önemsemez, doğru sayar.
isPassword = (password == girilenpassword.strip())

print(f"Email bilgisi doğru mu: {isEmail} Parola doğru mu {isPassword}")
