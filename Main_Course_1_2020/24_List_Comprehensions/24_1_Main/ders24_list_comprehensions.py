numbers = []
for x in range(10):
    numbers.append(x)
print (numbers)

# veya

numbers = [x for x in range(10)]
print(numbers)

# Yapılan adımlar
# 1- 0-10 arası sayılar tek tek alınır.
# 2- Alınan her değer x'in içine atılır.
# 3- x'in içine giren değer dizinin içindeki elemanları temsil eder.

for x in range(10):
    print(x**2)

# veya

numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x for x in range(10) if x%3==0]
print(numbers)

myString = "Hello"
myList = []

for letter in myString:
    myList.append(letter)
print(myList)

myList = [letter for letter in myString]
print(myList)

years = [1983,1999,2008,1956,1986]
ages = [2020-year for year in years]
print(ages)

results = [x if x%2==0 else "TEK" for x in range(1,10)]
print(results)

result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

numberz = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numberz)