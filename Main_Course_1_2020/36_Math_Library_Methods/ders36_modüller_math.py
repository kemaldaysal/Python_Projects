# pypi.org 'dan istediğimiz modülü, kütüphaneyi indirebiliriz.

import math # math modülünü dahil ettik

#value = dir(math) # modül içinde bulunan tüm fonksiyonları görme
#value = help(math)
#value = help(math.factorial)

value = math.sqrt(49) # 49'un karekökünü bul.
value = math.factorial(5)

import math as islem # math kütüphanesine islem takma adını verdik. math.sqrt yerine islem.sqrt kullanacağız.

value = islem.floor(5.9) # aşağı doğru yuvarlama
value = islem.ceil(5.9) # yukarı doğru yuvarlama

print(value)

### Yöntem 2 

def sqrt(x):
    print("x :"+str(x))

# from math import * # math kütüphanesinden hepsini içe aktar. math. Artık her şeyin başında kullanmamız gerekmeyecek.
from math import factorial,sqrt,ceil # math kütüphanesinden sadece 2 fonksiyonu import ettik. ceil metodu import edilmediğinden dolayı çalışmaz.

#value = factorial (5)
value = sqrt(9)

print(value)

