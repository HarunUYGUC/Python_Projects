def kelime_sayisini_bul():
    print("Kelime sayısını bulmak istediğiniz metni giriş yerine yapıştırmak daha iyi bir yöntem olabilir.")
    print("NOT: Kelimeler boşluklarla birbirinden ayrılır bu yüzden kelime olarak sayılabilmesi için başka kelimeyle arada boşluk olmalıdır.")

    metin = input("Metninizi giriniz.: ")
    kelime_listesi = metin.split()
    kelime_sayisi = len(kelime_listesi)
    print(f"Metindeki toplam kelime sayısı: {kelime_sayisi}")

    başkaMetinGirecekMi = input("Başka metin girmek istiyorsanız 'evet', istemiyorsanız 'hayır' yazınız.: ")

    if (başkaMetinGirecekMi == "evet"):
        kelime_sayisini_bul()
    else:
        print("Uygulama kapatıldı!")


programaGiriş = input("Metninizdeki kelime sayısını bulmak istiyorsanız 'evet', istemiyorsanız 'hayır' yazınız.: ")
programaGiriş = programaGiriş.lower()

if (programaGiriş == "evet"):
    kelime_sayisini_bul()
else:
    print("Uygulama kapatıldı!")