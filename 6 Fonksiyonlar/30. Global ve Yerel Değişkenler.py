
# fonksiyonlarda dışardaki değişkeni içerde kullanabiliyoruz fakat içerideki değişkeni dışarda kullanamıyoruz

a = 10


def fonksiyon():

    global a # dışarıdaki genel a yı tek seferde değiştiriyoruz
    a = 25
    
    print(a)



fonksiyon()