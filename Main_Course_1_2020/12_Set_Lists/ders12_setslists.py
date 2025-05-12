fruits = {"orange","apple","banana"}
# print(fruits) indekslenemez

for x in fruits:   #Liste içindeki elemanları sırasız şekilde yazdır.
   print(x)

fruits.add("cherry")
fruits.update(["mango","grape"])
print(fruits)

myList = [1,2,5,4,4,2,1]
print(myList)
print(set(myList)) # Set listede tekrarlayan elemanlar gösterilmez.

fruits.remove("mango")
fruits.discard("apple") # Remove yerine discard ile de silinebilir.
print(fruits)

fruits.pop() 
print(fruits)

fruits.clear # Listedeki tüm elemanlar silinir.
print(fruits)