message = 'Hello There. My name is Kemal Daysal'

message = message.upper() # Her şeyi büyük harfe çevirme
print(message)

message = message.lower() # Her şeyi küçük harfle yazma
print(message)

message = message.title() # Her kelimenin BAŞ HARFİ BÜYÜK olur.
print(message)

message = message.capitalize() # Sadece cümlenin ilk harfi büyük olur.
print(message)

message = message.strip() # Cümlenin başında boşluk karakteri varsa boşluğu siler.
print(message)

message = message.split() # Cümledeki her kelime ayrılır, boşluklardan bölünür. Her kelime bir dizi elemanı olarak kabul edilir.
print(message)
print(message[2])

#message = message.split('.') # Cümleyi noktaları referans alarak böler.
#print(message)

message = '---'.join(message) # Parçalı bilgileri birleştirecek ve araya çizgi ekleyecek.
print(message)

message = 'Hello There. My name is Kemal Daysal'
# index = message.find('Kemal') ## Kemal kelimesinin cümlede kaçıncı karakterde olduğunu belirtir.
isFound = message.startswith('H')
#print(index)
print(isFound)

isFound = message.endswith('z') #Cümle z ile mi bitiyor? Doğru/yanlış
print(isFound)

message = message.replace('Kemal','Zeynep') # Cümle içinde Kemal ifadesini bul ve yerine Zeynep yaz.
message = message.replace('a','d').replace('k','j')
print(message)

message = 'Hello There. My name is Kemal Daysal'
message = message.center(50,'*') # Mesajı ortalayıp sağ ve soluna * koy. 50, * miktarını veya pikselini belirtiyor?
print(message)





