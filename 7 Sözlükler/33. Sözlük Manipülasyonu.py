# Bu sözlüğe veri ekleme .setdefault()
'''
süper_lig = {"Galatasaray":"63 Puan","Fenerbahçe":"62 Puan","Beşiktaş":"61 Puan"}

süper_lig.setdefault("Trabzonspor","50 Puan")
süper_lig.setdefault("Petrolspor","90 Puan")

print(süper_lig)
'''
#---------------------------------------------------------------------------------
# İNPUT İLE EKLEME
'''

süper_lig = {"Galatasaray":"63 Puan","Fenerbahçe":"62 Puan","Beşiktaş":"61 Puan"}

takım_ekle = input("Takım Giriniz : ")
puan_ekle = input("Puan Giriniz :")

süper_lig.setdefault(takım_ekle,puan_ekle)



print(süper_lig)
'''
#---------------------------------------------------------------------------------
# VERİ SİLME
'''
süper_lig = {"Galatasaray":"63 Puan","Fenerbahçe":"62 Puan","Beşiktaş":"61 Puan"}

süper_lig.pop("Beşiktaş")

print(süper_lig)

'''

#---------------------------------------------------------------------------------
# yeni eklenen takımın birdaha silinmemesi için 

süper_lig = {"Galatasaray":"63 Puan","Fenerbahçe":"62 Puan","Beşiktaş":"61 Puan"}

while True:
    takım_ekle = input("Lütfen Takım Ekleyin : ")
    puan_ekle = input("Lütfen Puan Ekleyin : ")
    süper_lig.setdefault(takım_ekle,puan_ekle) # kişiden iki veri alıp bu verileri setdefautla süper_lig e ekledik  eklenen verileri while döngüsünün içine soktuk
    
    for i,j in süper_lig.items():
        print(i,j)

    seçim = input("Çıkmak İstermisiniz E/H : ")
    if seçim == "E":
        print("Çıkış Yapıldı...")
        break  # break döngünün durmasını yani bitirmesini sağlar
    else:
        pass #pass döngünün tekrar başa yani while başına dönmesini sağlar




