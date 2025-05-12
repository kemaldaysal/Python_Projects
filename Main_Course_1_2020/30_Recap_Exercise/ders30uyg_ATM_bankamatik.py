# Bankamatik Uygulaması

KemalHesap = {
    "ad":"Kemal Daysal",
    "hesapNo":"132134",
    "bakiye": 3000,
    "ekHesap": 2000
}

AliHesap = {
    "ad":"Ali Blabla",
    "hesapNo":"123456",
    "bakiye": 2000,
    "ekHesap": 1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] = hesap['bakiye'] - miktar
        print("Paranizi alabilirsiniz.")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanılsın mı? (e/h) ile cevaplayınız.")

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] = hesap['ekHesap'] - ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz.")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.")
        else:
            print("Bakiye yetersiz.")
            bakiyeSorgula(hesap)



def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL'dir.")

paraCek(KemalHesap,3000)
print("***********")
paraCek(KemalHesap,2000)
print("***********")
paraCek(KemalHesap,2000)