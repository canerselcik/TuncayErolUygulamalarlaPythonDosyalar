# AND OPERATÖRÜ

''' deneme = 8<10 and 12<11  

# and de eğer bir tanesi bile FALSE olursa false yazar
# her ikisi doğru ise TRUE
# her ikisi yanlış ise FALSE

print(deneme) '''

#------------------------------------------------------------------------------------

# AND(VE) OPERATÖRÜ ÖRNEK

''' db_şifre = 7272
db_adi = "batmani"

kullanıcı_adı = input("Lütfen Kullanıcı Adınızı Giriniz :")
kullanıcı_sifre = int(input("Lütfen Şifrenizi Giriniz :"))

kontrol = db_şifre==kullanıcı_sifre and db_adi== kullanıcı_adı

# db şifre eşitmidir kullanıcının girdiği şifreye
# ve db adi eşitmidir kullanıcı adına HERHANGİ BİRİSİ FALSE İSE FALSE YAZAR YOKSA TRUE YAZAR

print(kontrol) '''

#------------------------------------------------------------------------------------

# OR(VEYA) OPERATÖRÜ ÖRNEK

db_şifre = 2121
db_adi = "yusuf"

kullanıcı_adı = input("Lütfen Kullanıcı Adınızı Giriniz :")
kullanıcı_sifre = int(input("Lütfen Şifrenizi Giriniz :"))

kontrol = db_şifre==kullanıcı_sifre or db_adi== kullanıcı_adı

# db şifre eşitmidir kullanıcının girdiği şifreye
# ve db adi eşitmidir kullanıcı adına 
#İKİ DURUMDAN HERHANGİ BİRİSİ TRUE İSE TRUE YAZAR İKİSİ FALSE İSE FALSE YAZAR

print(kontrol)