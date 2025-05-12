# 1-100'e kadar sayıları ekrana yazdır.

#x = 0

#while x<100:
#    print(x)
#    x=x+1
#print("Bitti.")

#x = 50

#while x<=60:
#    print(x)
#    x=x+1
#print("Bitti.")

#x = 1
#while x<=100:
#    if x%2==1:
#        print(f"{x} sayısı tek.")
#    elif x%2==0:
#        print(f"{x} sayısı çift.")
#    x+=1
#print("Bitti.")

name = '' # name boşluk olursa False'a karşılık gelir.
while not name.strip(): # name içindeki boşluk yani false olduğu sürece döngü işlesin. Sürekli adını sorsun.
    name = input("İsminizi girin: ")
print(f"Merhaba {name}") 