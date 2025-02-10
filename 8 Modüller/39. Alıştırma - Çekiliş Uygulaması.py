import random
import time

kullanıcılar = list()

def kullanıcı_ekle(x):
    print("-"*30)
    print("Kullanıcı Ekleme Ekranına Hoşgeldiniz")
    ekle = input("Lütfen Eklenecek Kullanıcıyı Yazınız :")
    kullanıcılar.append(ekle)
    input("Devam Etmek İçin Enter Tuşuna Basınız...")

def kullanıcı_gör(x):
    say = 1
    print("-"*30)
    for i in x:
        print(str(say)+"-Kullanıcı Adı:",i)
        say+=1
    print("-"*30)
    input("Devam Etmek İçin Enter Tuşuna Basınız...")

def kullanıcı_sil(x):
    print("-"*30)
    print("Kullanıcı Silme Ekranına Hoşgeldiniz")
    sil = input("Lütfen Silinecek Kullanıcıyı Yazınız :")
    if sil in kullanıcılar:
        kullanıcılar.remove(sil)
        print(f"{sil} başarıyla silindi.")
    else:
        print(f"{sil} kullanıcı listesinde bulunamadı.")
    input("Devam Etmek İçin Enter Tuşuna Basınız...")

def seç(x):
    say = 1
    kişi_seç = int(input("Kaç Kişi Seçilsin ?"))
    if kişi_seç > len(x):
        print("Seçilecek kişi sayısı kullanıcı sayısından fazla olamaz.")
        return
    rastgele_seç = random.sample(x,kişi_seç)
    for i in rastgele_seç:
        print(str(say)+"- Kazanan Kullanıcı Adı:",i)
        say+=1
        print(" Diğer Kişi Sistemden Çekiliyor...")
        time.sleep(3)
    print("-"*30)
    input("Devam Etmek İçin Enter Tuşuna Basınız...")

def salla(x):
    print("-"*30)
    say = 1 
    random.shuffle(x)
    for i in x:
        print(str(say)+"-Kullanıcı Adı:",i)
        say+=1
    print("-"*30)
    input("Devam Etmek İçin Enter Tuşuna Basınız...")

while True:

    print("****ÇEKİLİŞ UYGULAMASINA HOŞGELDİNİZ****")
    seçim = int(input("1-Kullanıcı Ekle\n2-Kullanıcı Gör\n3-Kullanıcıları Karıştır\n4-Rastgele Sayı Seç\n5-Kullanıcı Sil\n6-Çıkış\n "))

    if seçim == 1:
        kullanıcı_ekle(kullanıcılar)
    elif seçim == 2:
        kullanıcı_gör(kullanıcılar)
    elif seçim == 3:
        salla(kullanıcılar)
    elif seçim == 4:
        print("Kişi Seçme Hesaplanıyor...")
        time.sleep(2)
        seç(kullanıcılar)
    elif seçim == 5:
        kullanıcı_sil(kullanıcılar)
    elif seçim == 6:
        print("Uygulamadan çıkılıyor...")
        break
    else:
        print("Lütfen Uygun Bir Tercih Yapınız...")
