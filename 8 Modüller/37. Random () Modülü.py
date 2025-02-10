# pythonun gömülü olan modülü random rastgele sayılar üretir

import random
'''

print(dir(random)) #RANDOM Modülünün İçindeki Fonksiyonları Görmek İçin

'''
#------------------------------------------------------------------------------------
'''
a = random.random() # 0-1 arasında rastgele sayı üretmek random parantezi parametre almaz

print(round(a*10,1)) # Burda 10 Demek 10 la çarp yani bir virgül kaydır demek virgülden sonraki 1 ise noktadan sonra yani 2.34565 gibi noktadan sonra kaç basamak göstereceğini belirtir

'''
#------------------------------------------------------------------------------------
'''
a = random.uniform(1.5,2.5) # uniform içine iki tane parametre alıyor

print(a)
'''

#------------------------------------------------------------------------------------
# tam sayı için
'''
a = random.randint(1,5) # bu sayılar arasında rastgele tam sayı oluştururu 1-5 dahil

print(a)
'''
#------------------------------------------------------------------------------------

'''
liste = ["Tuncay","Erol","Bilişim","Ordu","Galatasaray"]

a = random.choice(liste) # choice parantez içine yazılan listeden rastgele veri alır
print(a)
'''
#------------------------------------------------------------------------------------
'''
#listeyi karıştırır
liste = ["Tuncay","Erol","Bilişim","Ordu","Galatasaray"]

random.shuffle(liste)  # her seferinde  sırayı değiştirir karıştırır isimleri

print(liste)  

'''
#------------------------------------------------------------------------------------
#LİSTEDEN RASTGELE NUMUNE ALMA

liste = ["Tuncay","Erol","Bilişim","Ordu","Galatasaray"]

print(random.sample(liste,2))