def kg_lb_dönüştürücü():
    is_kg_to_lb = input("Kg'dan Lb'ye mi dönüştürmek istersin yoksa tersi mi? (Evet / Tersi): ")
    is_kg_to_lb.lower()

    if (is_kg_to_lb == "evet"):
        kg = 2.2   # 1 Kg = 2.2 Lb

        kacKg = int(input("Kaç kilogram olduğunu giriniz.: "))
        cevapLb = kacKg * kg
        print(f"{kacKg} kilogram = {round(cevapLb, 3)} Lb'dir.")
    
    elif (is_kg_to_lb == "tersi"):
        lb = 0.45359237   # 1 Lb = 0.45359237 Kg

        kacLb = int(input("Kaç Lb olduğunu giriniz.: "))
        cevapKg = kacLb * lb
        print(f"{kacLb} Lb = {round(cevapKg, 3)} Kilgoram'dır.")

    else:
        print("Hatalı cevap!")
        
    devamEdecekMi = input("Başka bir dönüştürme işlemi yapmak ister misin? (E / H): ")
    devamEdecekMi = devamEdecekMi.upper()

    if (devamEdecekMi == "E"):
        kg_lb_dönüştürücü()
    else:
        print("Uygulama kapatıldı!")
        

girecekMi = input("Kg-Lb dönüştürücüye girmek istiyor musun? (Evet / Hayır): ")
girecekMi = girecekMi.lower()

if (girecekMi == "evet"):
    kg_lb_dönüştürücü()
else:
    print("Uygulama kapatıldı!")
