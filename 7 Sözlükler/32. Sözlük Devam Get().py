'''
süper_lig = {"Galatasaray":"72 Puan","Fenerbahçe":"60 Puan","Beşiktaş":"57 Puan"}

takım = input("Lütfen Puanını Öğrenmek İstediğiniz Takımı Giriniz :").capitalize()

if takım not in süper_lig:
    print("Seçtiğiniz Takım Listemizde Bulunmamaktadır...")  # takım sorgular sözlükte varsa 9.satıra yoksa 6.satır yazdırılır.

else:
    print(takım,":",süper_lig[takım])

'''
#------------------------------------------------------------------------------------

süper_lig = {"Galatasaray":"72 Puan","Fenerbahçe":"60 Puan","Beşiktaş":"57 Puan"}

takım = input("Lütfen Puanını Öğrenmek İstediğiniz Takımı Giriniz :").capitalize()

print(takım,":",süper_lig.get(takım,"Belirttiğiniz Takım Puan Listemizde Bulunmamaktadır..."))

# süper_lig takım sözlüğünü ifade eder 

# .get() fonksiyonu parantez içine ilk önce takım var ise yani kullanıcıdan input ile aldığı takım var ise virgül öncesini yazdır eğer listede yok ise virgül sonrasını yazdır  


# bu gibi durumlarda if ve else kullanmamıza gerek kalmıyor


