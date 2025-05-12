# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
cars = ["BMW","Mercedes","Opel","Mazda"]
# 2- Liste kaç elemanlıdır?
print(len(cars))
# 3- Listenin ilk ve son elemanı nedir?
print(cars[0])
print(cars[-1])
# 4- Mazda değerini Toyota değeriyle değiştirin.
cars[-1] = "Toyota"
print(cars)
# 5- Mercedes listenin bir elemanı mıdır?
print("Mercedes" in cars)  # cars dizisinde Mercedes var mı sorgusu
# 6- Listenin -2 indeksindeki değer nedir?
print(cars[-2])
# 7- Listenin ilk 3 elemanını alın.
print(cars[0:3])
cars = ["BMW","Mercedes","Opel","Mazda"]
# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
cars[-2:] = ["Toyota","Renault"]
print(cars)
# 9- Listenin üzerine "Audi ve "Nissan" değerlerini ekleyin.
print(cars + ["Audi","Nissan"])
# 10- Listenin en son elemanını silin.
cars = ["BMW","Mercedes","Opel","Mazda"]
del cars[-1]
print(cars)
cars = ["BMW","Mercedes","Opel","Mazda"]
# 11- Liste elemanlarını tersten yazdırınız.
print(cars[::-1])
# 12- Aşağıdaki verileri bir liste içinde saklayınız.

   # studentA: Yiğit Bilgi 2010, (70,60,70)
   # studentB: Sena Turan 1999, (80,80,70)
   # studentC: Ahmet Turan 1998, (80,70,90)

studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,70]]
studentC = ["Ahmet","Turan",1998,[80,70,90]]

print(studentA[0])
print(studentB[1])
print(studentC[3][1]) # Listeler içi geçiş (studentC listesinin 3. elemanındaki dizinin 1. terimi) DİKKAT, SAYMA 0'DAN BAŞLIYOR

print(f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}")