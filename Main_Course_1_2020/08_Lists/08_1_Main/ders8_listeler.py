message = "Hello There. My name is Kemal Daysal".split()
#print(message[0])


my_list = ["bir",2,True,5.6]
print(my_list)
print()


list1 = ["one","two","three"]
list2 = ["four","five","six"]

numbers = list1 + list2
print(numbers)
print(len(numbers))
print(message[0])

userA = ["Kemal",19]
userB = ["Zeynep",10]

users1 = userA + userB # Klasik yol

print(userA)
print(userB)
print(users1)
print(users1[0][1]) # 0. listedeki 1. elemanı ekrana yazdır.

users2 = [userA, userB] # Liste içinde liste

print(userA)
print(userB)
print(users2)
print(users2[0][1]) # 0. listedeki 1. elemanı ekrana yazdır.


