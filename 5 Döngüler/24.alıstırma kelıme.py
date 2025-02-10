'''
# deneme.split()  verileri parçalar DENEMEYİ DÜZENLEMEK İSTİYORUM DEMEK deneme listesinin içindeki boşluklara göre sıralansın

deneme = "emir,erol,Galatasaray"

deneme = deneme.split(",") # split içine ne yazarsak parçalama ona göre yapılır 

print(deneme)

'''
# ['emir', 'erol', 'Galatasaray']

#------------------------------------------------------------------------------------

'''

tarih = "16/07/1991"

tarih = tarih.split("/")  # "/" GELEN YERLERİ AYIR BÖL DEMEK0

print(tarih)

#print(tarih[]) BURDA KARENİN İÇİNE 0-1-2 NE YAZILIRSA O SIRAYI YAZDIRIR 0 DAN BAŞLAR

'''

#------------------------------------------------------------------------------------
'''
veri_al = input(" Lütfen Parçalanacak Kelimeleri Yazınız : ")

for i in veri_al:
    print(i)

# alt alta harfleri yazar t u n ....

'''

#------------------------------------------------------------------------------------
'''

veri_al = input(" Lütfen Parçalanacak Kelimeleri Yazınız : ")

for i in veri_al.split(): # Bişey yazmadığımız için boşluklara göre ayrı demek 
   # tuncay
   #erol

    print(i)

    '''
#------------------------------------------------------------------------------------

veri_al = input(" Lütfen Parçalanacak Kelimeleri Yazınız : ")

for i in veri_al.split():
    print(i[0], end="")  # i harfi her gezdiği elementin 0.hanesini yazdırsın   
    # end="" birleştir anlamına gelir

