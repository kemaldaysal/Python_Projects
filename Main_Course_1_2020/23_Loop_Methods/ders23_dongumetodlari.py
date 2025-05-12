
### RANGE
# Range, Başlangıç sayısından,  girilen sayıya KADAR olan sayıları, 
# istenilen artış miktarıyla döngüye almayı sağlar.

for item in range(50,100,20): 
    print(item)

print(list(range(50,100,20))) # liste şeklinde yazdırma.


### ENUMERATE

index=0
greeting = "Hello"
for letter in greeting:
    print(f'İndex: {index} letter: {greeting[index]}')
    index = index + 1 

print("\n")
    # Üstteki kodlarla yapılan işi enumerate ile yapma

greeting = "Hello"
for index,letter in enumerate(greeting):
    print(f'İndex: {index} letter: {letter}')
      
print("\n")


#### ZIP
# Karşılılı gelen liste elemanlarını eşleştirme

list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
list3=[100,200,300,400,500]

print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(a,b)    

