# value types  => string, number

x = 5
y = 25

x = y # x'in içine y bilgisini attık.

y = 10 # y'de yapılan değişiklik x'i etkilemedi.
print(x,y)

# reference types => list, class
a = ["apple","banana"]
b = ["apple","banana"]

a = b 

b[0] = "grape" # y'de yapılan değişiklik x'i de değiştirdi.
print(a,b)