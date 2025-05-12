name = 'Kemal'
surname = 'Daysal'
age = 19


greeting = 'My name is ' + name + ' '+surname + ' and \nI am '+ str(age) +' years old.'
length = len(greeting)

#"""
print(greeting[0]) # Greeting'in 0. karakterini yazdır.
print(greeting[3])
print(len(greeting)) # Greeting'in kaç karakterli olduğunu ekrana yazdır
print(greeting[length-1])
# veya print(greeting[-1]) KISA YOL
print(greeting[3:7]) #Greeting'in içinden 3'ten 7'ye kadarki karakterleri ekrana yazdır.
print(greeting[3:]) # 3'ten sonsuza... uzaYa ve uzaGa
print(greeting[:16]) # Baştan 16'ya
print(greeting[2:40:2]) # * 2'den 40'a git, 2 karakterde bir olan karakterleri al, araları atla.
#"""