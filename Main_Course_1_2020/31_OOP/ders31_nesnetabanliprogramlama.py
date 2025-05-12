# Object Oriented Programming (OOP)

# class


class Person:
    pass  # Bunu yazdığımızda Person classı oluşturulur ancak içinde özellikleri boş geçilir. Uygulama hata vermez ancak class'ın içi boş olur.
    # class attributes
    address = "no information"

    # constructor (yapıcı metod)
    def __init__(
        self, name, year
    ):  # self'in anlamı class'tan üretilen p1 ya da p2 objesini temsil ediyor olmasıdır. Obje üstüne değer aktarılmak istenirse self kullanılır. Obje üstüne eklenilen attribute self'ten sonra yazılır.
        # object attributes
        self.name = name
        self.year = year
        print("init metodu çalıştı.")

    # methods


# object / instance

p1 = Person(name="Ali", year=1990)
p2 = Person(name="Yağmur", year=1995)

# updating
p1.name = "Ahmet"
p2.name = "Kemal"
p2.year = "2001"
p1.address = "Kocaeli"
p2.address = "Edirne"
# accessing and writing object attributes
print(f"p1: name: {p1.name} birth year: {p1.year} adres: {p1.address}")
print(f"p2: name: {p2.name} birth year: {p2.year} adres: {p2.address}")

print(p1)
print(p2)
