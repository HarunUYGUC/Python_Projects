import random

def sayiTahminOyunu(kullaniciAdi, istenenHak):
    oyunTanitimi = "0-100 arasındaki sayıyı bulma oyunu başladı!"
    print(oyunTanitimi)

    bulunacakSayi = random.randint(0, 100)
    birDenemeKacPuan = 100 / istenenHak
    birDenemeKacPuan = round(birDenemeKacPuan, 2)
    print(f"{kullaniciAdi}, her denemede {birDenemeKacPuan} puanın gidecektir. 100 üzerinden puanın oyun sonunda gösterilecektir.")

    kullanılanHak = 1
    while (kullanılanHak <= istenenHak):
        alınanPuan = 100 - ((kullanılanHak - 1) * birDenemeKacPuan)
        alınanPuan = round(alınanPuan, 2)
        kalanHak = istenenHak - kullanılanHak

        try:
            girilenTahmin = int(input(f"{kullaniciAdi}, tahmin ettiğin sayıyı gir: "))
        except ValueError:
            girilenTahmin = int(input(f"{kullaniciAdi}, hatalı tahmin, sayı girmelisiniz: "))
            
        if (girilenTahmin < 0) or (girilenTahmin > 100):
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
        print(f"{kullaniciAdi}, hakların bitti! Aldığın Puan: 0")

    tamamMiDevamMi = input(f"{kullaniciAdi}, oyuna devam etmek istiyorsan 'devam', istemiyorsan 'çık' yaz.")

    if (tamamMiDevamMi.lower() == "devam"):
        print(f"{kullaniciAdi}, oyun baştan başladı.")
        istenenHak = int(input(f"{kullaniciAdi}, bu sefer kaç hak ile oynamak istersin?: "))
        sayiTahminOyunu(kullaniciAdi, istenenHak)
    elif (tamamMiDevamMi.lower() == "çık"):
        print(f"{kullaniciAdi}, oyun kapatıldı.")


kullaniciAdi = input("0-100 arası Sayı Tahmin oyununu oynamak için kullanıcı adınızı giriniz: ")
istenenHak = int(input(f"{kullaniciAdi}, oyunu kaç hak ile oynamak istersin?: "))
sayiTahminOyunu(kullaniciAdi, istenenHak)
