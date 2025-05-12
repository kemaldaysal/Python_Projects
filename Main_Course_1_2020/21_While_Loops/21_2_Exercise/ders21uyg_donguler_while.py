sayilar = [1,3,5,7,9,12,19,21]
# 1- sayilar listesini while ile ekrana yazdırın.

#i = 0
#while (i < len(sayilar)):
#    print(sayilar[i])
#    i=i+1

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki
#    tüm tek sayıları ekrana yazdırın.


#baslangic = int(input("Başlangıç değerini girin: "))
#bitis = int(input("Bitiş değerini girin: "))
#
#i = baslangic
#while i<bitis:
#    i = i + 1
#    if(i%2==1):
#        print(i)
    

# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın.

#i = 100
#while i>0:
#    i = i-1
#    print(i)

# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.

#numbers = []

#i = 0
#while i < 5:
#    sayi = int(input("Sayı girin: "))
#    numbers.append(sayi) # Her girilen sayıyı numbers dizisine ekleme
#    i = i + 1
#numbers.sort() # Liste içindeki sayıları otomatik sıralama
#print(numbers)


# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler
#    listesi içinde saklayınız
#    *** Ürün sayısını kullanıcıya sorun.
#    *** Dictionary listsei yapısı ( name, price) şeklinde olsun.
#    *** Ürün ekleme işlemi bittiğinde ürünleri ekranda while ile
#        sıralayın.

urunler = []

adet = int(input("Kaç ürün eklemek istiyorsunuz? : "))
i = 0 

while(i<adet):
    name = input("Ürün ismi: ")
    price = int(input("Ürün fiyatı: "))
    urunler.append({
        "name" : name,
        "price": price
    })
    i = i + 1

for urun in urunler:
    print(f'Ürün adı: {urun["name"]}, ürün fiyatı: {urun["price"]}')