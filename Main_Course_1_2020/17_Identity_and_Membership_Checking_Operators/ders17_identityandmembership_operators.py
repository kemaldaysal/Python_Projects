# Identity operator: is

x = y = [1,2,3]
z = [1,2,3]

print(x==y)
print(x==z)
print(x is y) # x ile y'yi karşılaştırır, X'in içeriği y'ye eşit mi? sorusunu sorar.
print(x is z ) # Dizi içeriği aynı olsa bile false değerini veriyor. Objelerin aynı olup olmadığı sorgulanır. Adresleri farklıdır.

a = [1,2,3]
b = [2,4]

del a[2]
b[1] = 1
b.reverse()
print(a==b)
print(a is b)
print(a is not b) 

# Membership operator: in

x = ["apple","banana"]
print("banana" in x)

name = "Kemal"
print("a" in name) # name değişkeni içindeki bilgide "a" var mı?
print("z" not in name)


