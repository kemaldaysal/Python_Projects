with open("newfile.txt","r",encoding="UTF-8") as file:  # with ile kod bloğu oluşturduk. Artık file.close() 'a ihtiyacımız yok. with içindeki komutlar bittiğinde dosya otomatik kapanacak.
    content = file.read()
    print(content)
    file.seek(0) # İmlecin GİDECEĞİ YERİ belirleme. 0 yazarsak içeriğin en başına döner. Böylece içeriği tekrar okutabiliriz.
    print(file.tell()) # İmlecin anlık konumunu gösterir.
    content2 = file.read()
    print(content2)

# *** r+ ile güncelleme yapılack dosyada dosyanın içeriği write'taki gibi silinmez. Üzerine eklenir.