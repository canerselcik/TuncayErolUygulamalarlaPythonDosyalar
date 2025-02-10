# İÇ İÇE KOŞUL 

ateş_durumu =(float(input("Lütfen Ateş Derecenizi Yazınız : ")))  
öksürük = input("Öksürüğünüz Var Mı ? E/H : ").lower()
baş_ağrısı = input("Baş Ağrınız Varmı ? E/H : ").lower()
gün = int(input("Şikayetleriniz Kaç Gündür Var ? :"))


if ateş_durumu>=39:
    if gün>=3:
        print("*** Uyarı Hastaneye Gidiniz")
    else:
        print("Ateş Durumunuz Sınırda ,Devam Ederse En Yakın Sağlık Kuruluşuna Gidiniz")

if (ateş_durumu>=39)and (öksürük=="e") and (baş_ağrısı=="e") and (gün>=3):
    print("***ACİL Lütfen En Yakın Sağlık Kuruluşuna Gidiniz..")
    print("***ACİL Durumunuz Olumlu Değil..")

elif (öksürük=="e") or (baş_ağrısı=="e") or (gün>=3):
    print("*** Hatırlatma Durumunuz Bu Şekilde Devam Ederse Lütfen Sağlık Kuruluşuna Gidiniz..")

else:
    print("Ateş Durumunuz 39 Derecenin Üzerine Çıkarsa En Yakın Hastaneye Gidiniz ")
    print(f"Ateşiniz : {ateş_durumu}")