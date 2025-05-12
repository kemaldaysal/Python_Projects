name = "Kemal Daysal"

for letter in name:
    if letter == "a":  # name'i yazarken a'ya denk geldiği anda
        break          # döngüyü durdur. 
    print(letter)
print("\n")
name = "Kemal Daysal"

for letter in name:
    if letter == "a":  # name'i yazarken a'ya denk geldiği anda
        continue       # döngüyü a'yı atlayarak devam ettirir.
    print(letter)      # a'yı ekrana yazdırmaz.

print("\n")

x = 0
while x < 5:
    x+=1  
    if x==2:
        continue
    print(x)
      

# 1'den 100'e kadar tek sayıların toplamı.      

z=0
toplam = 0

while (z<100):
    z+=1
    if(z%2==0):
        continue 
    toplam = toplam + z
    
print(f"Toplam: {toplam}")