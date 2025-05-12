mylist = [1,2,3]
myString = "my string"

print(len(mylist))
print(len(myString))
print(type(mylist))
print(type(myString))


class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu.")

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self): ## Silindiğini belli eden dönüt
        print("Film silindi.")

m = Movie("Film adı","yönetmen adı",120)

#print(str(mylist))
print(str(m))

del m # m objesini sildik.

print(m)
