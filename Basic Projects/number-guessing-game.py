import random

def sayiTahminOyunu(kullaniciAdi):
    oyunTanitimi = "0-100 arasındaki sayıyı bulma oyunu başladı!"
    print(oyunTanitimi)

    while True:
        try:
            istenenHak = int(input(f"{kullaniciAdi}, oyunu kaç hak ile oynamak istersin?: "))
        except ValueError:
            print(f"{kullaniciAdi}, hatalı bir değer! Sayı girmelisin.!")
        except Exception:
            print("Bİlinmeyen bir hata oluştu!")
        else:
            break

    bulunacakSayi = random.randint(0, 100)
    birDenemeKacPuan = 100 / istenenHak
    birDenemeKacPuan = round(birDenemeKacPuan, 2)
    print(f"{kullaniciAdi}, her denemede {birDenemeKacPuan} puanın gidecektir. 100 üzerinden puanın oyun sonunda gösterilecektir.")

    kullanılanHak = 1
    while (kullanılanHak <= istenenHak):
        alınanPuan = 100 - ((kullanılanHak - 1) * birDenemeKacPuan)
        alınanPuan = round(alınanPuan, 2)
        kalanHak = istenenHak - kullanılanHak

        while True:
            try:
                girilenTahmin = int(input(f"{kullaniciAdi}, tahmin ettiğin sayıyı gir: "))
            except ValueError:
                print(f"{kullaniciAdi}, hatalı bir değer! Sayı girmelisin!")
            except Exception:
                print("Bilinmeyen bir hata oluştu!")
            else:
                break
                    
        while (girilenTahmin not in range(0, 101)):
            girilenTahmin = int(input(f"{girilenTahmin} hatalı bir tahmin. 0-100 arasında bir sayı giriniz: "))

        if (girilenTahmin == bulunacakSayi):
            print(f"Tebrikler {kullaniciAdi}, bulunacak sayı {bulunacakSayi}'idi. Aldığınız Puan: {alınanPuan}")
            break
        elif (girilenTahmin < bulunacakSayi):
            print(f"{kullaniciAdi}, sayıyı büyütmelisin. {kalanHak} Hakkınız Kaldı!")
        elif (girilenTahmin > bulunacakSayi):
            print(f"{kullaniciAdi}, sayıyı küçültmelisin. {kalanHak} Hakkınız Kaldı!")
        
        kullanılanHak += 1

    if (kalanHak == 0):
        print(f"{kullaniciAdi}, hakların bitti! Aldığın Puan: 0 / Bulunacak sayı {bulunacakSayi}'idi.")

    tamamMiDevamMi = input(f"{kullaniciAdi}, oyuna devam etmek istiyorsan 'devam', istemiyorsan 'çık' yaz.")

    if (tamamMiDevamMi.lower() == "devam"):
        print(f"{kullaniciAdi}, oyun baştan başladı.")
        istenenHak = int(input(f"{kullaniciAdi}, bu sefer kaç hak ile oynamak istersin?: "))
        sayiTahminOyunu(kullaniciAdi, istenenHak)
    else:
        print(f"{kullaniciAdi}, oyun kapatıldı.")


kullaniciAdi = input("0-100 arası Sayı Tahmin oyununu oynamak için kullanıcı adınızı giriniz: ")
sayiTahminOyunu(kullaniciAdi)
