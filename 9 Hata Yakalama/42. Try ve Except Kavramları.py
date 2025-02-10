

try:
    sayı1= int(input("Sayı1:"))
    sayı2= int(input("Sayı2:"))

    toplam = sayı1/sayı2

    print(toplam)

    
    # except ZeroDivisionError:
    # print("Bir Sayı Sıfıra Bölünemez...")

    # except ValueError:
    # print("Lütfen Sayı Giriniz.")
    # # burda özel hatalar gösterilir
    

    # tek satırda birden fazla hata yazmak için 

except (ZeroDivisionError,ValueError):
    print("Hata Var...")

