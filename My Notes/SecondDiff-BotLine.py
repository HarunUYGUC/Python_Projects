# İki farklı zaman arasındaki saniye farkını hesaplamak için aşağıdaki gibi kod 
# yazılmalı.

import datetime

first_date = datetime.datetime.now()
print(first_date)

merhaba = input("Merhaba yaz: ")
print(merhaba)

second_date = datetime.datetime.now()
print(second_date)


difference_in_seconds = (second_date - first_date).total_seconds()
print(difference_in_seconds)


# print() içerisine yazdığımız uzun bir metni Terminal'de yan yana değil de
# alt alta görmek istiyorsak o iki şey arasına \n şeklinde aşağıdaki gibi bir 
# komut yazmalıyız. 

# \n sağındaki metne yapışık olursa alt satıra geçen o metnin başlangıcında
# boşluk olmaz iken boşluk bırakırsak bir karakterlik boşluk oluşur. 

print(f"First Date: {first_date} \nSecond Date: {second_date} \nSeconds Difference: {difference_in_seconds}")
