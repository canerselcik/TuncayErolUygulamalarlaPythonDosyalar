
def su_hesapla(kilo): # parametre 25.satırda aldığımız kiloyu buraya veriyoruz
    erkek_hesapla = kilo*0.04
    kadın_hesapla = kilo*0.03

    cinsiyet = input("Lütfen Cinsiyetinizi Giriniz : Kadın/Erkek : ").lower() # loer ile yazılan erkek kadını küçülttük

    if cinsiyet == "erkek":
        print("-"*30)
        print("Cinsiyetiniz : ",cinsiyet)
        print(erkek_hesapla,"Litre Su İçmelisiniz...")
        print("-"*30)
    elif not cinsiyet:
        print("Cinsiyetsiz Olmaz Cinsiyetinizi Giriniz :))")

    elif cinsiyet =="kadın":
        print("-"*30)
        print("Cinsiyetiniz :",cinsiyet)
        print(kadın_hesapla,"Litre Su İçmelisiniz...")
        print("-"*30)

kilo_iste = int(input("Lütfen Kilonuzu Giriniz :")) # kulllanıcıdan input ile kiloyu alıyoruz 

su_hesapla(kilo_iste)
