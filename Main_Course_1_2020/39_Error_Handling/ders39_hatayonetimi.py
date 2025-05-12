# error types


# ERROR
# print(a) => NameError
# int("1a2") => ValueError
# print(10/0) => ZeroDivisionError 
# print("denem"e) => SyntaxError



# error handling 

try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)

except ZeroDivisionError:
    print("y değeri için 0 girilemez. Uygulama kapatılıyor.")

except ValueError:
    print("x ve y için sadece sayısal değer girmelisiniz.")


print("**************")
### HATA GRUPLAMA ve HANGİ HATANIN MEYDANA GELDİĞİNİ SÖYLEME
#except (ZeroDivisionError,ValueError) as e:
#    print("Yanlış bilgi girdiniz.")
#    print(e)

### TÜM HATALARA KARŞI BİLDİRİM *** Burada hatanın türü tespit edilemez. except as e: print(e) yapılamaz.
#except:
#   print("Yanlış bilgi girdiniz.")
#else:
#   print("Her şey yolunda.") # HATA YOKSA 


while True:
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        print(a/b)
    except Exception as ex:
        print("Yanlış bilgi girdiniz. Hata sebebi:",ex)
    else:  
        break
    finally:
        print("try except sonlandı.")
