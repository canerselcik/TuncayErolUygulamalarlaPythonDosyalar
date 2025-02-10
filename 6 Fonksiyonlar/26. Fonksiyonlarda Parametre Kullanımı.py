
# kullanıcıdan isim soyisim meslek ve yaş ile alakalı değişken alacağız
'''
ad = input("Lütfen Adınızı Giriniz : ")
soyadı = input("Lütfen Soyadınızı Giriniz : ")
yaş = input("Lütfen Yaşınızı Giriniz : ")
meslek = input("Lütfen Mesleğinizi Giriniz : ")

'''

def kullanıcı_bilgileri(ad,soyad,yaş,meslek):
    print(f"Adınız : {ad}\nSoyadınız : {soyad}\nYaşınız : {yaş}\nMesleğiniz :{meslek}")
    print("-"*30)



ad = input("Lütfen Adınızı Giriniz : ")
soyad = input("Lütfen Soyadınızı Giriniz : ")
yaş = input("Lütfen Yaşınızı Giriniz : ")
meslek = input("Lütfen Mesleğinizi Giriniz : ")

# def deki verileri 17.satırdaki aldığımız verilerle dolduruyoruz her seferinde tek tek yazmamıza gerek yoktur.

kullanıcı_bilgileri(ad,soyad,yaş,meslek)
