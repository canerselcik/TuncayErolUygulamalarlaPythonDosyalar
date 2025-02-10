
# ALIŞTIRMA KULLANICIDAN ŞİFRE OLUŞTURMASINI İSTEYECEĞİZ ŞİFRE EN AZ 3 EN FAZLA 8 KARAKTERLİ OLMASINI İSTEYECEĞİZ


for i in range(3):
    şifre = input("Lütfen Şifre Belirleyiniz : ")


    if not şifre: 
        print("Bu alan boş bırakılamaz!! ")
    # EĞER ŞİFRE BOŞ İSE BU ALAN GÖSTERİLİR

    elif len(şifre) in range(3,8):
        print("Yeni Şifreniz : ",şifre)
        break
    #BURDA ŞİFRE UZUNLUĞU LEN İLE SAYILIR 3-8 ARASINDAYSA ŞİFRE KULLANICIYA VERİLİR VE BREAK İLE KOMUTTAN ÇIKILIR.

    
    
    elif i==2:
    # Burda en başta range(3) komutu ile "i" 3 defa dönsün dedik burda i==2 dedik çünkü i saymaya 0 dan başlar ilk denemede 0 sonra 1 sonra 2 ve3 sonra 3 e gelince aşağıdaki print yazdırılır
        print("Şifreyi 3 Kere Yanlış Girdiniz Şifreniz Bloke Oldu Daha Sonra Tekrar Deneyiniz ")
       
    else:
        print("Şifreniz 8 Karakterden Uzun Yada 3 Karakterden Kısa")
        
        #EĞER ŞİFRE 3-8 ARASINDA DEĞİLSE BURDA GEZEN İ HARFİ ARTAR HER ARTTIĞINDA BUNU YAZAR EĞER HAK DOLDUĞU ZAMAN DENEME 3 Ü GEÇERSE 20.SATIRA DÖNER VE ORASI YAZDIRILIR