"""

# Object Oriented Programming (OOP)

# class

class Person:
    pass # Bunu yazdığımızda Person classı oluşturulur ancak içinde özellikleri boş geçilir. Uygulama hata vermez ancak class'ın içi boş olur.
    # class attributes
    address = "no information"


    # constructor (yapıcı metod)
    def __init__(self,name,year): # self'in anlamı class'tan üretilen p1 ya da p2 objesini temsil ediyor olmasıdır. Obje üstüne değer aktarılmak istenirse self kullanılır. Obje üstüne eklenilen attribute self'ten sonra yazılır.
        # object attributes
        self.name = name
        self.year = year
        print("init metodu çalıştı.")

    # methods
    def intro(self):
        print("Hello there. I am "+self.name)

    def calculateAge(self):
        return 2019 - self.year

# object / instance

p1 = Person(name="Ali",year=1990)
p2 = Person(name="Yağmur",year=1995)

p1.intro()
p2.intro()

print(f"Adım: {p1.name} ve yaşım: {p1.calculateAge()}")
print(f"Adım: {p2.name} ve yaşım: {p2.calculateAge()}")
"""

class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self,yaricap=1):
        self.yaricap = yaricap

    # Methods
    def cevre_hesapla(self):
        return 2 * self.pi + self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle(5) # ifade belirtilmezse yaricap = 1 olur. 
c2 = Circle() 

print(f"c1: Alan = {c1.alan_hesapla()} Çevre = {c1.cevre_hesapla()}")
print(f"c2: Alan = {c2.alan_hesapla()} Çevre = {c2.cevre_hesapla()}")


