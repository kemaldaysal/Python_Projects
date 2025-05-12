website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?
# 2- 'website' içinden www karakterlerini alın.
# 3- 'website' içinden com karakterlerini alın.
# 4- 'course' içinden ilk 15 ve son 15 karakterleri alın.
# 5- 'course' ifadesindeki karakterleri tersten yazdırın.

print(len(course))
length = len(website)
print(website[7:10]) # veya result = website[7:10]
print(website[22:25]) # veya sondan saymak için önce
print(website[length-3:length])

print(course[:15])
print(course[-15:])

print(course[::-1]) # 2 yazarsak 2 karakterde bir alacak.

# BURASI ANLAŞILMADI, AŞAĞIYA TEKRAR BAK
s = '12345' * 5 
print(s[::5]) # Sadece 5. değeri yani sonraki ifadedeki ilk değeri yazdır.

s = '12345' * 8 
print(s[::5]) # Sadece 5. değeri yani sonraki ifadedeki ilk değeri yazdır.

#################################################################################

name, surname, age, job = 'Kemal','Daysal',19,'öğrenci'

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#   'Benim adım Kemal Daysal, yaşım 19 ve mesleğim öğrenci

print(f'Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}.')
print("Benim adım "+name +" "+surname+", yaşım "+str(age)+" ve mesleğim "+job+".")
print("Benim adım {0} {1}, yaşım {2} ve mesleğim {3}.".format(name,surname,age,job))
# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

s = "Hello World"
s = s[0:6] + 'W' + s[-4:]
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
result = 'abc' * 3
print(result)
