def hesap_makinesi():
    islemTurleri = ["toplama", "çıkarma", "çarpma", "bölme"]

    islemTuru = input("Toplama mı, çıkarma mı, çarpma mı, bölme mi yapmak istersiniz?: ")
    islemTuru = islemTuru.lower()

    while (islemTuru not in islemTurleri):
        islemTuru = input("Hatalı cevap! Toplama mı, çıkarma mı, çarpma mı, bölme mi yapmak istersiniz?: ")
        islemTuru = islemTuru.lower()

    while True:
        try:
            sayi1 = float(input("1. Sayınızı Giriniz: "))
            sayi2 = float(input("2. Sayınızı Giriniz: "))
        except ValueError:
            print("Yanlış bir değer girdiniz! Sayı girmelisiniz!")
        except Exception as e:
            print("Bilinmeyen bir hata oluştu!")
            print(e)
        else:
            break

    if (islemTuru == "toplama"):
        sonuc = sayi1 + sayi2
    elif (islemTuru == "çıkarma"):
        sonuc = sayi1 - sayi2
    elif (islemTuru == "çarpma"):
        sonuc = sayi1 * sayi2
    elif (islemTuru == "bölme"):
        try:
            sonuc = sayi1 / sayi2
        except ZeroDivisionError:
            print("Bölme işleminde 2. sayı yani bölen 0 (sıfır) olamaz!")
            sonuc = "Sonuç Hesaplanamadı"
            print(sonuc)

    if (type(sonuc) != str):
        print(f"{sonuc:,}")

    yeniBirİslem = input("İşlem yapmaya devam etmek istiyorsan 'devam', istemiyorsan 'çık' yazmalısın!: ")

    if (yeniBirİslem == "devam"):
        hesap_makinesi()
    else:
        print("Hesap makinesi kapatıldı!")
        

hesap_makinesi()