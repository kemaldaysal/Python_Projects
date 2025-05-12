list = [1,2,3]

tuple = (1, "iki",3)

print(type(list))
print(type(tuple))

print(list[1])
print(tuple[1])

print(len(list))
print(len(tuple))

list = ["ali","veli"]
tuple = ["damla","ayşe","ayşe"]
names = ["demet","emel","ayşe"] + tuple

print(names)

list[0] = "ahmet"
tuple[0] = "deniz" 
# tuple türü listelere eleman yerine
# başka bir değer ataması yapılamaz, desteklenmez. 
# Başta atanır ve öylece kalır, tek bir eleman 
# değiştirilemez. ? Artık destekleniyor mu? 

print(tuple.count("ayşe"))
print(tuple.index("ayşe"))

print(list)
print(tuple)