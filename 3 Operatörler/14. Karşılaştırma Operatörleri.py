
#  == : Eşitmidir

"""db = 7272

kullanıcı_şifre = int(input("Lütfen Şifrenizi Giriniz :"))

kontrol = db == kullanıcı_şifre

print(kontrol)  """

# dbde bir şifre vardır sonra kullanıcıdan input ile şifre ister 
# sonra bu şifreyi  db  ile kullanıcı_şifre eşitmidir diye  kontrol eder 
# eğer eşitse TRUE değilse FALSE döndür

# -----------------------------------------------------------------------------------

#EŞİT DEĞİLDİR OPERATÖRÜ

# != Eşitdeğilmidir

"""db = 7272
kb = 12345

kontrol = db != kb
print(kontrol)  """

# -----------------------------------------------------------------------------------

#KÜÇÜKTÜR OPERATÖRÜ

# < KÜÇÜKMÜDÜR    

"""yas = 17

kontrol = yas<17

print(kontrol) """

#<= KÜÇÜK YADA EŞİTMİDİR

"""yas = 20

kontrol = yas<=21

print(kontrol) """

# -----------------------------------------------------------------------------------

#BÜYÜKTÜR OPERATÖRÜ

# > BÜYÜKMÜDÜR

"""yas = 51

kontrol = yas>=50

print(kontrol)"""

#<= BÜYÜK YADA EŞİTMİDİR

""" yas = 12

kontrol = yas>=17

print(kontrol)  """

# -----------------------------------------------------------------------------------

# ÖRNEK

liste = [1,2,3,4]
liste2 = [1,2,3,4,5]

kontrol = len(liste)<len(liste2)   #len uzunluk belirtir  liste nin uzunluğu liste1 den küçükmü diye sorduk

print(kontrol)