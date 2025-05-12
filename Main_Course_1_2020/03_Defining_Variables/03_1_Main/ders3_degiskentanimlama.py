maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli*vergi))
print(maasAhmet - (maasAhmet*vergi))

# Değişken Tanımlama Kuralları (Yorum Satırı)
# Değişken ifade ismi rakam ile başlayamaz. 1number = 10 yapılamaz.
# Aynı değişken 2 kere tanımlanamaz.
# Değişken tanımlarken boşluk olamaz, alt çizgi kullanılabilir.

number1 = 10 # Geçersiz kaldı, aşağıda 20 tanımlandı.
print(number1)
number1 = 20
print(number1)

number1 += 30 # number1 = number1 + 30
print(number1)

# Sayılar '6' gibi string şeklinde yazılırsa harf gibi kabul edilir,
# program bunların sayı olduğunu ayırt edemez ve matematik işlemi yapmaz.

a = '10'
b = '20'
print(a+b) # Sonuç 1020 olarak çıkıyor, 30 çıkmıyor

firstName = "Kemal"
lastName = " Daysal"
print(firstName + lastName) 

# Değişkenler tek satırda tanımlanabilir.

x = 1               #int
y = 2.3             #float
name = "Kemal"      #string
isStudent = True    #bool

# x ,y , name, isStudent = (1, 2.3, Kemal, True)
