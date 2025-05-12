"""

# aradığımız ve okumak istediğimiz dosya, aranan yerde yoksa hata verir. Bu hatayı hata yönetimi ile düzelterek uygun bir hata kodu vermesini sağlayabiliriz.
try:
    file = open("newfile2.txt","r") # sonunda ,"r" yazmasak bile varsayılan olarak okuma halindedir. "r" yazmasak da olur.
    print(file)
except FileNotFoundError:
    print("Dosya okuma hatası. Dosya, belirtilen konumda bulunamadı.")
finally:
    print("Dosya kapandı.")
    file.close()

"""

file = open("newfile.txt","r",encoding="UTF-8")

# for döngüsüyle okuma

"""
for i in file:  # Bir şey yazmazsak arada boşluk bırakarak ekrana dosya içindekileri yazar. Bunun sebebi print fonksiyonu işlemini bitirdikten sonra bir boş satır bırakır.
    print(i,end="") # Print, işini bitirdikten sonra sona boşluk koymasını engelledik.
"""

# read() fonksiyonuyla okuma
"""
content = file.read()

print("İçerik 1")
print(content)

file = open("newfile.txt","r",encoding="UTF-8")
content2 = file.read()
print("İçerik 2")
print(content2)
file.close()
"""
### 2. içeriği okumaya çalıştığında hiçbir şey okumaması, 1. içeriği okuduktan sonra imlecin, dosyanın en sonuna gitmiş olmasıdır. Dosya hala kapanmadığından sondaki boşlukları okur.
### içerik 2'ye de dosyayı okumak istersek, içerik 2'nin tanımlamasından önce dsoyayı tekrar açtırmamız gerekir.

"""
content = file.read(5) # Dosyadaki yazının ilk 5 karakterini oku.
content = file.read(3) # Önceki komutta 5. karakterin sonuna gelmiştik. Böylece imleç orada kaldı. 3 karakter daha oku dersek, SONRAKİ 3 karakteri okur. Baştan okumaz.
content = file.read(3)
print(content)
file.close()
"""

# readline() fonksiyonu
"""
print(file.readline(),end="") # Dosya içindeki yazının İLK SATIRINI okuma
print(file.readline(),end="") # Kaldığı konumdan okumaya devam etme
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),)
print(file.readline(),)
print(file.readline(),)
print(file.readline(),)
file.close()
"""

# readlines() fonksiyonu
"""
liste = file.readlines() # Satırdaki HER BİLGİYİ (\n vs. dahil) okuma

print(liste)
print(liste[0])
print(liste[1])
print(liste[2])
file.close()
"""
