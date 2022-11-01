def vucut_kitle_indeksi():
    while True:
        try:
            kilo = float(input("Kilonuzu kilogram cinsinden giriniz (Örn: 56): "))
            boy = float(input("Boyunuzu metre cinsinden giriniz (Örn: 1.74): "))
        except ValueError:
            print("Harf değil sayı girmelisiniz! Tekrar deneyiniz.")
        except Exception:
            print("Bilinmeyen bir hata oluştu! Tekrar deneyiniz.")
        else:
            break

    hesapSonucu = kilo / boy**2
    hesapSonucu = round(hesapSonucu, 2)

    if (hesapSonucu < 18.5):
        print(f"Sonuç: {hesapSonucu} - Yani 'ZAYIFSINIZ!!!'")
    elif (hesapSonucu >= 18.5) and (hesapSonucu < 25):
        print(f"Sonuç: {hesapSonucu} - Yani 'NORMALSİNİZ!!!'")
    elif (hesapSonucu >= 25) and (hesapSonucu < 30):
        print(f"Sonuç: {hesapSonucu} - Yani 'KİLOLUSUNUZ!!!'")
    elif (hesapSonucu >= 30):
        print(f"Sonuç: {hesapSonucu} - Yani 'AŞIRI KİLOLUSUNUZ!!!'")


giris = input("'Vücut Kitle İndeksi' hesaplamasını yapmak ister misiniz? (Evet / Hayır): ")
if (giris.lower() == "evet"):
    vucut_kitle_indeksi()
else:
    print("Uygulama kapatıldı!")
