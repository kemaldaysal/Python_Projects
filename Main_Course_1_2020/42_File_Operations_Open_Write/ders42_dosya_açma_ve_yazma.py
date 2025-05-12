# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w" : (Write) yazma modu. Dosyayı konumda oluşturur.
# *** Mevcut dosya içeriğindekileri siler ve son yazılan komuttaki içeriği üzerine yazar.
# *** file.write içine bir şey yazılmadıysa, program çalıştığı anda içindeki her şey silinir.
"""
file = open("newfile.txt","w")
file = open("C:/Users/kemal/AppData/Local/Programs/Python/Python38-32/Python_Projeleri/newfile.txt","w")
file.close() # Dosyayı açtıktan sonra dosyayı kapatmak gerekir.
"""

"""
file = open("newfile.txt","w",encoding="UTF-8") 
file.write("Kemal Daysal")
file.close()
"""

# "a" : (Append) ekleme. Dosya konumda yoksa oluşturur. Dosya içinde daha önce olan veriyi SİLMEDEN üzerine ekleme işlemi.

"""
file = open("newfile.txt","a",encoding="UTF-8") # UTF-8, Türkçe karakter içeren karakter seti.
file.write("\nZeynep Daysal")
file.close()
"""

# "x" : (Create) oluşturma. Belirtilen konumda oluşturulacak dosya zaten varsa uygulama hata verir, yenisini oluşturmaz.

file = open("newfile2.txt","x",encoding="UTF-8") 


# "r" : (Read) okuma. Varsayılan: Dosya konumda yoksa hata verir.
