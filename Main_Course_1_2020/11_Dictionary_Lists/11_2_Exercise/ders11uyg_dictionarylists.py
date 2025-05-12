# 1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
# 2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

# 2. Yol
#ogrenciler[number] = {
#    "ad":name,
#    "soyad":surname,
#    "telefon":phone
#}

ogrenciler.update({
    number: {
        "ad":name,
        "soyad":surname,
        "telefon":phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        "ad":name,
        "soyad":surname,
        "telefon":phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        "ad":name,
        "soyad":surname,
        "telefon":phone
    }
})

print("*"*50)

ogrNo = input("öğrenci no: ") # Üstte yazılanlar arasından seçim
ogrenci = ogrenciler[ogrNo]
print(ogrenci)
print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")

# ' ve " olayları değiştiriyor, dikkat et