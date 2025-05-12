'''
 1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı 
 ifadeleri ile buldurmaya çalışın.
 ** "random modülü" için "python random" şeklinde arama yapın.
 ** 100 üzerinden puanlama yapın. Her soru 20 puan
 ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen
    can sayısı üzerinden hesaplansın.
'''

import random

sayi=random.randint(1,100)
can = int(input("Kaç hak kullanmak istersiniz? "))
hak = can
sayac=0

while hak > 0:
    hak = hak - 1
    sayac = sayac + 1
    tahmin=int(input("Sayıyı tahmin edin: "))

    if sayi == tahmin:
        print(f"Tebrikler, {sayac}. tahmininizde bildiniz! Toplam puanınız: {100-(100/can) * (sayac-1)}")
        break
    elif sayi > tahmin:
        print("Tahmin ettiğiniz sayıyı arttırmalısınız.")
    else:
        print("Tahmin ettiğiniz sayıyı azaltmalısınız.")

    if hak == 0:
        print(f"Hakkınız bitti. Tutulan sayı: {sayi}")



