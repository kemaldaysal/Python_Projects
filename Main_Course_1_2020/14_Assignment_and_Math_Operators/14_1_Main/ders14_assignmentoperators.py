x, y, z = 5, 16, 20

print(x, y, z)

#x,y = y,x # x'in yerine y, y'nin yerine x'i koy.
x = x + 5 # x+=5 ile aynı şeydir.
y -= 4
z *= 3
z /= 2
x %= 5 # 5 değeri 5'e bölündüğünde kalan 0 olduğundan 0 sonucunu verir.
y //= 5
y **= 5 # üs alma operatörü yani y^5

print(x,y,z)

values = 1,2,3,4,5
print(values)
print(type(values))

a,b,*c = values # 1=>x , 2=>b , 3,4,5 => c ye gitti. 
print(a,b,c)

