
süt_miktarı = int(input("Lütfen Elinizde Olan Süt Miktarını Yazınız (Litre) :"))

kaşar_peyniri_limiti = 11

if süt_miktarı<kaşar_peyniri_limiti:
    print("Süt Miktarınız Kaşar Peynir Yapmak İçin Uygun Değil : ") ,süt_miktarı
    print("Kaşar Peynir Üretmek İçin Eksik Olan Süt Miktarı : " ,kaşar_peyniri_limiti-süt_miktarı)

else:
    toplam_üretim = süt_miktarı/kaşar_peyniri_limiti
    print(f"Toplam Kaşar Miktarı (Kg) : {int(toplam_üretim)}")
