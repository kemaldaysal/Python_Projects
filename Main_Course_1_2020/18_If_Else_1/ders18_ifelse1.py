username = "kd"
password = "123"

gusername=input("Kullanıcı adınızı giriniz: ")
gpassword=input("Parolanızı giriniz:")

if (gusername == username):
    if (gpassword == password):
        print("Hoş geldiniz.")
    else:
        print("Parolanız yanlış.")
else:
    print("Kullanıcı adınız yanlış.")


