numbers = [1,10,5,16,4,9,10]
letters = ["a","g","s","b","y","a","s"]

valmin = min(numbers)
valmax = max(numbers)
print(valmin)
print(valmax)

letmax = max(letters)
letmin = min(letters)
print(letmax)
print(letmin)

val = numbers[3:6]
print(val)
val2 = numbers[:3]
print(val2)
val3 = numbers[4:]
print(val3)

numbers[4] = 40 #Numbers dizisinin 5. elemanını 40 ile değiştirdik.

numbers.append(49)
numbers.append(69)
numbers.append(36) # Dizinin sonuna terim ekleme
print(numbers)

numbers.insert(3, 78) # 3. index yani 4. terimden hemen önce 78 elemanını diziye ekle.
print(numbers)
numbers.insert(-1,52) # Son terimden önce 52 ekledik.
print(numbers)

numbers.pop() # Son terimi diziden silme
print(numbers)
numbers.pop(0) # Parantez içinde istenilen elemanı silme
print(numbers)

numbers.remove(49) # Listeden 49 sayısını bul ve sil.
print(numbers)

numbers.sort() # Numaraları küçükten büyüğe sırala.
print(numbers)

letters.sort() # Harfleri alfabetik sıraya göre sırala.
print(letters)

numbers.reverse() # Numarları küçükten büyüğenin tersinde yani büyükten küçüğe yazdır.
print(numbers)

letters.reverse()
print(letters)

print(numbers.count(10)) # Numbersın içinde kaç tane 10 rakamı var?
print(letters.count("a"))

