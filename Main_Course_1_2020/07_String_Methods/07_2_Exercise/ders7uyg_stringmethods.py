website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan sona Python Programlama Rehberiniz (40 saat)"


# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
message = " Hello World ".strip()
print(message)
message = " Hello World ".lstrip() # Soldaki boşluğu silme
print(message)
message = " Hello World ".rstrip() # Sağdaki boşluğu silme
print(message)

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi disinda her karakteri silin.

print('www.sadikturan.com'.strip('w.moc')) # Parantez içinde belirtilen karakterleri metinden sil.

# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
print(course.lower()) # Her kelimeyi küçük yaz
print(course.upper()) # Her kelimeyi büyük yaz
print(course.title()) # Kelimelerin sadece baş harflerini büyük yaz.

# 4- 'website' içinde kaç tane a karakteri vardır? (count('a'))

print(website.count('a')) # Cümlede kaç tane a var?
print(website.count('t')) 
print(website.count('www')) # Cümlede kaç tane 'www' var? 
print(website.count('www',0,10)) # Cümlede 0 ile 10. karakter arasında www karakterlerinin kaç tane olduğunu bul ve ekrana yazdır.

# 5- 'website' "www" ile başlayıp com ile bitiyor mu? 

print(website.startswith("www")) # Website değişkeni www ile başlıyor mu? 
print(website.startswith("http"))
print(website.endswith("com")) # Website değişkeni com ile bitiyor mu?

# 6- 'website' içinde '.com' ifadesi var mı?

print(website.find("com"))
print(website.find("com",0,10)) # Website'ın 0-10 karakterleri arasında com ifadesi var mı? # Bulamadığı için -1 değerini verir.
print(course.find("Python"))
print(course.rfind("Python")) #Python ifadesi sağdan yani cümlenin sonundan başına doğru kaçıncı sırada?
print(website.index("com"))
print(website.rindex("com"))

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

course = "Python Kursu: Baştan sona Python Programlama Rehberiniz (40 saat)"
print(course.isalpha()) # Kurs ifadesi harflerden mi oluşuyor?
print("Hello".isalpha())
print(course.isdigit()) # Kurs ifadesi rakamlardan mı oluşuyor?
print("123".isdigit())


# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

print("Contents".center(50,"*"))
print("Contents".ljust(50,"*")) # İfadeyi sola yasla, sağına yıldızları ekle.
print("Contents".rjust(50,"*")) # İfadeyi sağa yasla, soluna yıldızları ekle.

# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

print(course.replace(" ", "-")) # Boşluk olan her yere - koy.

# 10- "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştirin.

print("Hello World".replace("World","There"))

# 11- "course" karakter dizisini boşluk karakterlerinden ayırın.

result = course.split(" ")
print(result)
print(result[5])