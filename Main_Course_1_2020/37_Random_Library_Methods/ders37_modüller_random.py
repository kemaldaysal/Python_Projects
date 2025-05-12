import random

#result = dir(random)
#result = help(random)

result = random.random() # varsayılan: 0,0 - 1,0 arasında rastgele sayı üretir.
result = random.random() * 100 # (+10 dersek sayı 0 yerine 10'dan başlar.) üretilen sayı her seferinde 100 ile çarpılacak. Böylece 0-100 arası sayı üretilmiş olacak
result = int(random.uniform(10,20)) # 10-20 arası ondalıklıdan tamsayıya çevrilmiş sayı
result = random.randint(1,100) # 1-100 arası üretilmiş TAMSAYI

# Listeden rastgele eleman seçme
greeting = "Hello There"  
names = ["Ali","Yağmur","Deniz","Cenk","Ahmet","Efe"]
result = names[random.randint(0,len(names)-1)] # -1 dememizin sebebi listenin 4 elemanlı olup, ilk elemanının 0, son elemanının 3 olarak kabul edilmesi. -1 koymayınca eğer rastgele sayı 4 gelirse liste sınırları dışına çıkıldığından uygulama hata veriyor.
result = random.choice(names) # Liste içinden rastgele elemanı kısa yolla seçme.
result2 = random.choice(greeting) # Hello There kelimesinden rastgele harfler çekecek.

print(result + " " + result2 + ".")

liste = list(range(10))
random.shuffle(liste) # Liste içindeki elemanların yerlerini karıştırır
result = liste 

print(result)

liste = range(100)

result = random.sample(liste, 3) # Liste içinden 3 tane rastgele eleman çek.
print(result)
result = random.sample(names, 3)
print(result)


