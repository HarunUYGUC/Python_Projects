import random

def tas_kagit_makas(kullaniciAdi):
    print(f"{kullaniciAdi}, oyuna hoş geldin. Bilgisayara karşı 3 zafer alan kazanır.")
    oyununOlasiliklari = ["taş", "kağıt", "makas"]

    oyuncununZaferi = 0
    bilgisayarinZaferi = 0

    while (oyuncununZaferi < 3) and (bilgisayarinZaferi < 3):
        bilgisayarinCevabi = random.choice(oyununOlasiliklari)
        oyuncununCevabi = input("Cevabınızı giriniz: ")
        oyuncununCevabi = oyuncununCevabi.lower()

        while (oyuncununCevabi not in oyununOlasiliklari):
            oyuncununCevabi = input(f"{kullaniciAdi}, taş-kağıt-makas harici bilgi girmemelisin. Yeni cevabını girebilirsin: ")
            oyuncununCevabi = oyuncununCevabi.lower()

        if (oyuncununCevabi == "taş") and (bilgisayarinCevabi == "makas"):
            print(f"Tebrikler {kullaniciAdi}, kazandın! Bilgisayarın Cevabı: {bilgisayarinCevabi} - Senin Cevabın: {oyuncununCevabi}")
            oyuncununZaferi += 1
            print(f"Bilgisayarın Zaferi: {bilgisayarinZaferi} - Senin Zaferin: {oyuncununZaferi}")
    
        elif (bilgisayarinCevabi == "taş") and (oyuncununCevabi == "makas"):
            print(f"Üzgünüm {kullaniciAdi}, kazanamadın! Bilgisayarın Cevabı: {bilgisayarinCevabi} - Senin Cevabın: {oyuncununCevabi}")
            bilgisayarinZaferi += 1
            print(f"Bilgisayarın Zaferi: {bilgisayarinZaferi} - Senin Zaferin: {oyuncununZaferi}")
            
        elif (oyuncununCevabi == "taş") and (bilgisayarinCevabi == "taş"):
            print(f"{kullaniciAdi}, berabere! Bilgisayarın Cevabı: {bilgisayarinCevabi} - Senin Cevabın: {oyuncununCevabi}")
            print(f" Bilgisayarın Zaferi: {bilgisayarinZaferi} - Senin Zaferin: {oyuncununZaferi}")
            

        if (oyuncununCevabi == "kağıt") and (bilgisayarinCevabi == "taş"):
            print(f"Tebrikler {kullaniciAdi}, kazandın! Bilgisayarın Cevabı: {bilgisayarinCevabi} - Senin Cevabın: {oyuncununCevabi}")
            oyuncununZaferi += 1
            print(f"Bilgisayarın Zaferi: {bilgisayarinZaferi} - Senin Zaferin: {oyuncununZaferi}")
            
        elif (bilgisayarinCevabi == "kağıt") and (oyuncununCevabi == "taş"):
            print(f"Üzgünüm {kullaniciAdi}, kazanamadın! Bilgisayarın Cevabı: {bilgisayarinCevabi} - Senin Cevabın: {oyuncununCevabi}")
            bilgisayarinZaferi += 1
            print(f"Bilgisayarın Zaferi: {bilgisayarinZaferi} - Senin Zaferin: {oyuncununZaferi}")
            
        elif (oyuncununCevabi == "kağıt") and (bilgisayarinCevabi == "kağıt"):
            print(f"{kullaniciAdi}, berabere! Bilgisayarın Cevabı: {bilgisayarinCevabi} - Senin Cevabın: {oyuncununCevabi}")
            print(f"Bilgisayarın Zaferi: {bilgisayarinZaferi} - Senin Zaferin: {oyuncununZaferi}")
            

        if (oyuncununCevabi == "makas") and (bilgisayarinCevabi == "kağıt"):
            print(f"Tebrikler {kullaniciAdi}, kazandın! Bilgisayarın Cevabı: {bilgisayarinCevabi} - Senin Cevabın: {oyuncununCevabi}")
            oyuncununZaferi += 1
            print(f" Bilgisayarın Zaferi: {bilgisayarinZaferi} - Senin Zaferin: {oyuncununZaferi}")
            
        elif (bilgisayarinCevabi == "makas") and (oyuncununCevabi == "kağıt"):
            print(f"Üzgünüm {kullaniciAdi}, kazanamadın! Bilgisayarın Cevabı: {bilgisayarinCevabi} - Senin Cevabın: {oyuncununCevabi}")
            bilgisayarinZaferi += 1
            print(f"Bilgisayarın Zaferi: {bilgisayarinZaferi} - Senin Zaferin: {oyuncununZaferi}")
            
        elif (oyuncununCevabi == "makas") and (bilgisayarinCevabi == "makas"):
            print(f"{kullaniciAdi}, berabere! Bilgisayarın Cevabı: {bilgisayarinCevabi} - Senin Cevabın: {oyuncununCevabi}")
            print(f"Bilgisayarın Zaferi: {bilgisayarinZaferi} - Senin Zaferin: {oyuncununZaferi}")
            
    if (oyuncununZaferi == 3):
        print(f"{kullaniciAdi}, tebrikler oyunu {oyuncununZaferi}'e karşı {bilgisayarinZaferi} ile kazandınız!")
    elif (bilgisayarinZaferi == 3):
        print(f"{kullaniciAdi}, oyunu {bilgisayarinZaferi}'e karşı {oyuncununZaferi} ile kaybettiniz!")

    tamamMiDevamMi = input(f"{kullaniciAdi}, oyuna devam etmek istiyorsan 'devam', istemiyorsan 'çık' yaz.")

    if (tamamMiDevamMi.lower() == "devam"):
        print(f"{kullaniciAdi}, oyun baştan başladı.")
        tas_kagit_makas(kullaniciAdi)
    else:
        print(f"{kullaniciAdi}, oyun kapatıldı.")


kullaniciAdi = input("Taş-kağıt-makas oyununu oynamak için kullanıcı adınızı giriniz: ")
tas_kagit_makas(kullaniciAdi)
