import datetime

def yazma_hizi_hesaplayici():
    print("- AÇIKLAMA: Aşağıdaki metni gördüğün anda yazmaya başlamalısın, bitince de 'Enter a' basmalısın. \n- 100 kelimelik olan bu metni kaç saniyede ve ne kadar doğru yazdığın önemlidir.")
    metniGor = input("Metni görmek için 'Evet' yazmalısın: ")
    
    if (metniGor.lower() == "evet"):
        metin = "Şehrin en işlek caddesinde, yarım asırlık bir pasajın en alt katında, babadan kalma küçük bir çay ocağı işletiyordu. Müşterileri genellikle cadde üzerinde bulunan dershanenin öğrencileri veya pasajdaki diğer esnaflar oluyordu. Sabah sekiz, akşam altı derken günü tatlı bir yorgunlukla bitirip, ardından evinin yolunu tutuyordu. Evde onu sabırsızlıkla bekleyen biri beş, diğeri sekiz yaşında olan iki oğlu vardı. Ne var ki dedelerini hiç görmediklerinden ara sıra kendi oğullarına, babasını anlatıyordu. Bir sabah caddenin başında, bir fotoğraf sergisinin kurulduğunu gördü. O gün sırf merakından o sergiyi gezmek istedi. Çocuklarına hiçbir zaman gösteremediği dedelerinin, çay ocağının önünde çekilmiş siyah beyaz bir fotoğrafı duruyordu."
        metninKelimeListesi = metin.split()
        print(metin)
        
        baslangicAni = datetime.datetime.now()
        baslangicAninSaati = datetime.datetime.strftime(baslangicAni, "%X")
        print(baslangicAninSaati)

        girilenMetin = input("Metni girmeye başla: ")
        girilenMetininKelimeListesi = girilenMetin.split()

        dogruGirilenKelimeSayisi = 0
        i = 0
        while (i < 99):
            if (metninKelimeListesi[i] == girilenMetininKelimeListesi[i]):
                dogruGirilenKelimeSayisi += 1
            else:
                pass
        
        bitisAni = datetime.datetime.now()
        bitisSaati = datetime.datetime.strftime(bitisAni, "%X")

        gecenSure = bitisSaati - baslangicAninSaati
        print(f"Geçen Süre: {gecenSure} \nDoğru Yazılan Kelime: {dogruGirilenKelimeSayisi}")
        
        wps = dogruGirilenKelimeSayisi / gecenSure # word per second (saniyedeki kelime sayısı)
        print(f"WPS (Saniyedeki Kelime Sayısı) = {wps}")
        
        dogruluk = 100 - dogruGirilenKelimeSayisi
        print(f"%{dogruluk} Doğruluk")
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
