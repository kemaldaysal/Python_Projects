# global scope
x = 'global x'

def function():
    #local scope
    x = 'local x'
    print(x)

function()
print(x)

#global
name = "Kemal"

def changeName(new_name):
    #local
    name = new_name
    print(name)

changeName("Zeynep")
print(name)

#################### PROGRAM YERELDEN --> GENELE DOĞRU İÇ İÇE FONKSİYONU ÇALIŞTIRIR.

name = "global string"

def greeting():
    #name = "Çınar"

    def hello():
        # name = "Ada"
        print("Hello " + name)

    hello()

greeting()

###################

x = 50
def test():
    global x #x bilgisinin global halini değiştirmek için bunu yaptık. Artık fonksiyon içinde yapılan işlemler dışarıya tamamen yansır.
    print (f"x : {x}")

    x = 100
    print(f"changed x to {x}")

test()
print(x)

