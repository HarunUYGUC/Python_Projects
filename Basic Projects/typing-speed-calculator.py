import datetime

def yazma_hizi_hesaplayici():
    print("- AÇIKLAMA: Aşağıdaki metni gördüğün anda yazmaya başlamalısın, bitince de 'Enter a' basmalısın. \n- 100 kelimelik olan bu metni kaç saniyede ve ne kadar doğru yazdığın önemlidir.")
    metniGor = input("Metni görmek için 'Evet' yazmalısın: ")
    print("*" * 10)
    
    if (metniGor.lower() == "evet"):
        metin = "Şehrin en işlek caddesinde, yarım asırlık bir pasajın en alt katında, babadan kalma küçük bir çay ocağı işletiyordu. Müşterileri genellikle cadde üzerinde bulunan dershanenin öğrencileri veya pasajdaki diğer esnaflar oluyordu. Sabah sekiz, akşam altı derken günü tatlı bir yorgunlukla bitirip, ardından evinin yolunu tutuyordu. Evde onu sabırsızlıkla bekleyen biri beş, diğeri sekiz yaşında olan iki oğlu vardı. Ne var ki dedelerini hiç görmediklerinden ara sıra kendi oğullarına, babasını anlatıyordu. Bir sabah caddenin başında, bir fotoğraf sergisinin kurulduğunu gördü. O gün sırf merakından o sergiyi gezmek istedi. Çocuklarına hiçbir zaman gösteremediği dedelerinin, çay ocağının önünde çekilmiş siyah beyaz bir fotoğrafı duruyordu."
        metninKelimeListesi = metin.split()
        print(metin)
        
        baslangicAni = datetime.datetime.now()
        girilenMetin = input("Metni girmeye başla: ")
        bitisAni = datetime.datetime.now()
        girilenMetninKelimeListesi = girilenMetin.split()
        print("*" * 10)

        bayrak = "HATA YOK"
        dogruGirilenKelimeSayisi = 0
        i = 0
        while (i < len(girilenMetninKelimeListesi)):
            try:
                if (metninKelimeListesi[i] == girilenMetninKelimeListesi[i]):
                    dogruGirilenKelimeSayisi += 1
                    i += 1
                else:
                    i += 1
            except IndexError:
                print("Hatalı giriş! Metindekinden fazla kelime girdiniz.")
                bayrak = "HATA"
                break
            except Exception:
                print("Bilinmeyen bir hata!")
                bayrak = "HATA"
                break
        
        if (bayrak == "HATA YOK"):
            gecenSure = (bitisAni - baslangicAni).total_seconds()

            print(f"Geçen Süre: {gecenSure} \nYazılan Kelime: {len(girilenMetninKelimeListesi)} \nDoğru Yazılan Kelime: {dogruGirilenKelimeSayisi}")
            print("-" * 10)

            wps1 = dogruGirilenKelimeSayisi / gecenSure # word per second (saniyedeki kelime sayısı)
            print(f"WPS (Saniyedeki Doğru Kelime Sayısı) = {round(wps1, 2)}")
        
            wps2 = len(girilenMetninKelimeListesi) / gecenSure # word per second (saniyedeki kelime sayısı)
            print(f"WPS (Saniyedeki Yazılan Kelime Sayısı) = {round(wps2, 2)}")

            dogruluk = dogruGirilenKelimeSayisi / len(girilenMetninKelimeListesi) * 100
            print(f"% {round(dogruluk, 2)} Doğruluk")
        else:
            print("Uygulama kapatıldı!")
    else:
        print("Uygulama kapatıdı!")

    tekrarDeneyecekMi = input("Tekrar denemek ister misin? (E / H): ")

    if (tekrarDeneyecekMi.lower() == "e"):
        yazma_hizi_hesaplayici()
    else:
        print("Uygulama kapatıldı!")


girecekMi = input("Yazma hızını öğrenmek ister misin? (Evet / Hayır): ")

if (girecekMi.lower() == "evet"):
    yazma_hizi_hesaplayici()
else:
    print("Uygulama kapatıldı")



"""
Önemli bulduğum ve yeni öğrendiğim kısa yollar. :D
"""
# Indent Line (Girinti oluşturmak): CTRL + Ü
# Move Line Up (Satırı yukarıya taşımak): ALT + UpArrow
# Move Line Down (Satırı aşağıya taşımak): ALT + DownArrow
