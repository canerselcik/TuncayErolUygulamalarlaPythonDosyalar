tel_rehberi = dict()

def te_no_ekle (x): # x tel_rehberini ifade eder
    print("***NUMARA EKLEME EKRANINA HOŞGELDİNİZ***")
    numara_isim_al = input("Lütfen Kayıt Edilecek Kişinin Adını Yazınız : ")
    numara_no_al = input("Lütfen Telefon Numarasını Giriniz : ")
    input("Devam Edilsin mi?")


    x= tel_rehberi.setdefault(numara_isim_al,numara_no_al) # x yazma nedeni dışardan x alıp oraya bağlamak bu x telefon rehberi  
    # .setdefault ile boş listemize değer ekliyoruz
    print(f"{numara_isim_al}'adlı kişi telefon listesine eklendi...")



def tel_rehber_göster(x): # x yukarıdaki rehberi ifade eder içindeki itemler for yapısıyla gezsin 

    kişi_sayısı = len(x)
    print(f"Rehberinizdeki Kayıtlı Kişi Sayısı  : {kişi_sayısı}")
    print("Rehbere Hoşgeldiniz")
    
    for i,j in x.items():
        print(i,":",j)
    input("Devam Edilsin mi?")

def no_sil(x):
    print("Kişi Silme Ekranına Hoşgeldiniz")
    silinecek_kişi = input("Silinecek Kişiyi Yazınız : ") # input ile bir değişken ismi alıyoruz
    x= tel_rehberi.pop(silinecek_kişi) # x değişkenini telefon rehberiyle eşitliyoruz
    input("Devam Edilsin mi?")
# .pop ile input ile kullanıcıdan aldığımız silinecek_kişiyi sil (.POP PARANTEZİN İÇİNE YAZANI SİLER)


while True:
    print("***HOŞGELDİNİZ***")
    print("***Seçim Yapınız***")
    seçim_yap = int(input("1-Ekle\n2-Sil\n3-Rehberi Gör\n"))

    if seçim_yap == 1 :
        te_no_ekle(tel_rehberi)

    elif seçim_yap == 2 :
        no_sil(tel_rehberi)
    
    elif seçim_yap == 3 :
        tel_rehber_göster(tel_rehberi)
        print("*"*30)
    else:
        print("Hatalı Tuşlama Yaptınız Lütfen Belirtilen Tuşlara Basınız..")