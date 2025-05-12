name = "Kemal"
surname = "Daysal"
age = 19

#print('My name is {} {}'.format(name,surname))
#print('My name is {1} {0}'.format(name,surname))
print('My name is {s} {n} and I am {a} years old.'.format(n=name, s=surname, a=age))
print('My name is {} {} and I am {} years old.'.format(name,surname,age))

result = 200/700
print("The result is {r:1.3}".format(r=result)) #3 bilgisi virgülden sonra kaç basamak olacağını söyler. Sol kısım ise tam kısım için baştan kaç karakterlik boşluk bırakılacağını belirtir. 
print("The result is {r:10.4}".format(r=result)) 
print("The result is {r:1.4}".format(r=result)) 

print(f"My name is {name} {surname} and I'm {age} years old.") # f string ile kolayca yazma.