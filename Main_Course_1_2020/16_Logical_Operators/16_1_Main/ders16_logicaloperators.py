x = 8

hak = 0
devam = 'e'
result = 5 < x < 10

# and

result = (x > 5) and (x < 10) # x 5'ten büyük mü? , x 10'dan küçük mü? True olması için her ikisi de sağlanmalı. 
result = (hak > 0) and (devam == 'e')
#True, True => False
#True,False => False ## False baskın.

# or 

result = (x > 0) or (x % 2 == 0) 
# ikisinden biri doğruysa sonuç doğru olur.
# True, False => True
# True, True => True
# False, False => False

# not

result = not(x > 0) # Cevabın tersini alır. Cevap True ise false olur.

# x, 5-10 arasında olan bir çift sayı mı?ü

result=((x>5) and (x<10)) and (x%2==0)

print(result)