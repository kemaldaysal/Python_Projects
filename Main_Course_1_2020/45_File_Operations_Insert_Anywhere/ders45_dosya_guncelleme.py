"""
with open("newfile.txt","r+",encoding="UTF-8") as file: # r+ , hem yazma hem okuma modunu açar.
    file.seek(20)
    file.write("deneme"))

with open("newfile.txt","r+",encoding="UTF-8") as file: # r+ , hem yazma hem okuma modunu açar.
    print(file.read())
"""

### Sayfa sonunda güncelleme

"""
with open("newfile.txt","a",encoding="UTF-8") as file:
    file.write("\nEmel Turan")
with open("newfile.txt","r",encoding="UTF-8") as file: # r+ , hem yazma hem okuma modunu açar.
    print(file.read())
"""

### Sayfa başında güncelleme

"""
with open("newfile.txt","r+",encoding="UTF-8") as file:
    content = file.read()
    content =  "Efe Turan\n" + content 
    file.seek(0)
    file.write(content)

with open("newfile.txt","r",encoding="UTF-8") as file:
    print(file.read())
"""

### Sayfa ortasında güncelleme

with open("newfile.txt","r+",encoding="UTF-8") as file:
    list = file.readlines()
    list.insert(1,"Kemal Daysal\n")
    file.seek(0)
    for i in list:
        file.write(i)

with open("newfile.txt","r",encoding="UTF-8") as file:
    print(file.read())
    