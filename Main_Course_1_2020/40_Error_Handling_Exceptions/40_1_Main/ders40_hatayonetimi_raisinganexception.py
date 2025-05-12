#x = 10
#if x > 5:
#    raise Exception("x, 5'ten büyük değer alamaz.")

def check_password(psw):
    import re
    if len(psw) < 7:
        raise Exception("Parola en az 7 karakter olmalıdır.")
    elif not re.search("[a-z]",psw): # Parola 7 karakterden uzun ve küçük harf içermiyor ise
        raise Exception("Parola küçük harf içermelidir.")
    elif not re.search("[A-Z]",psw): 
        raise Exception("Parola büyük harf içermelidir.")
    elif not re.search("[0-9]",psw): 
        raise Exception("Parola rakam içermelidir.")
#    elif re.search("\s",psw): # Parola boşluk (\s) içeriyorsa
#        raise Exception("Parola boşluk içermemelidir.")
    else:
        print("Parola geçerli.")

password = "1234567aB"

try: 
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Geçerli parola: else")
finally: # Ne olursa olsun yazdırılacak.
    print("Doğrulama tamamlandı.")