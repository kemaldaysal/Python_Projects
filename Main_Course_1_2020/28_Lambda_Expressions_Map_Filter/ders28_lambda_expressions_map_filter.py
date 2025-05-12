# def square(num): return num ** 3

#numbers = [1,3,5,9]

#result = list(map(square,numbers))
#print(result)

# ya da 
# for item in map(square,numbers):
#     print(item)



# lambda kullanımı

square = lambda num: num**2

numbers = [1,3,5,9,10,4]

#result = list(map(lambda num:num **2,numbers))

#result = square(6)

check_even = lambda num: num%2==0

result=list(filter(lambda num: num%2==0, numbers))

print(result)

