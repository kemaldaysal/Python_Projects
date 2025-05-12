
"""
def cube():
    for i in range(5):
        yield i ** 3 # bir değer üret ve ürettiğin her değerin küpünü al. Ürettiğin değeri bellekte depolama, ürettiğin gibi kullan, harca.


for i in cube():
    print(i)
"""

# Oluşturduğumuz değeri, liste içine saklamak gerekmiyorsa, elemanı anlık kullanıp sonra ihtiyaç duymayacaksak
# generator kullanmalıyız.

generator = (i**3 for i in range(5))
print(generator)

for i in generator:
    print(i)

# ya da
"""
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
"""