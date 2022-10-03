def kg_lb_donusturucu():
    is_kg_to_lb = input("Kg'dan Lb'ye mi dönüştürmek istersin yoksa tersi mi? (Evet / Tersi): ")
    is_kg_to_lb.lower()

    if (is_kg_to_lb == "evet"):
        kg = 2.2   # 1 Kg = 2.2 Lb

        while True:
            try:
                kacKg = float(input("Kaç kilogram olduğunu giriniz.: "))
                cevapLb = kacKg * kg
                print(f"{kacKg} kilogram = {round(cevapLb, 3)} Lb'dir.")
            except ValueError:
                print("Hatalı giriş! Sayı girmelisiniz!")
            except Exception:
                print("Bİlinmeyen bir hata!")
            else:
                break
    
    elif (is_kg_to_lb == "tersi"):
        lb = 0.45359237   # 1 Lb = 0.45359237 Kg

        while True:
            try:
                kacLb = float(input("Kaç Lb olduğunu giriniz.: "))
                cevapKg = kacLb * lb
                print(f"{kacLb} Lb = {round(cevapKg, 3)} Kilgoram'dır.")
            except ValueError:
                print("Hatalı giriş! Sayı girmelisiniz!")
            except Exception:
                print("Bilinmeyen bir hata!")
            else:
                break

    else:
        print("Hatalı cevap!")
        
    devamEdecekMi = input("Başka bir dönüştürme işlemi yapmak ister misin? (E / H): ")
    devamEdecekMi = devamEdecekMi.upper()

    if (devamEdecekMi == "E"):
        kg_lb_donusturucu()
    else:
        print("Uygulama kapatıldı!")
     

girecekMi = input("Kg-Lb dönüştürücüye girmek istiyor musun? (Evet / Hayır): ")
girecekMi = girecekMi.lower()

if (girecekMi == "evet"):
    kg_lb_donusturucu()
else:
    print("Uygulama kapatıldı!")
