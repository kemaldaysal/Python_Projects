""" 
    Yarıçapı verilen bir dairenin alan ve çevresini hesaplayınız. (r= 3.14)"""

pi = 3.14
r = float(input("Yari capi girin: ")) ## İnputtan bilgi okunduğunda string şekilde gelir, numbera çevrilmesi gerekli.
alan = pi * (r ** 2)
cevre = 2 * pi * r

print("Alan: " + str(alan) + " Çevre: " + str(cevre))



