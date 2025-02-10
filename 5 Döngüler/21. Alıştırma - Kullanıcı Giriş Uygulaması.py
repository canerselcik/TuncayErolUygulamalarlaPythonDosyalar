
ig_ka = "batmani"  #instagram kullanıcı adı
ig_ps = 7272       #instagram şifresi


while True:   #while döngüsüne girer

    kullanıcı_adı = input("Lütfen Kullanıcı Adınızı Giriniz : ") 
    #kullanıcı adı istenir
    kullanıcı_ps = int(input("Lütfen Şifrenizi Giriniz : "))  
    #şifre istenir
 
    
    if ig_ka == kullanıcı_adı and ig_ps == kullanıcı_ps:  
        # and(ve) hem kullanıcı adı hem şifre doğruysa hoşgeldiniz kullanıcı adını yazdırır
        print("Hoşgeldiniz :",kullanıcı_adı)
        break   # komutu durdurur çünkü if bitti istediğimiz oldu
    
    
    
    elif ig_ka != kullanıcı_adı and ig_ps == kullanıcı_ps:  
        # != eşit değildir yani ig_ka ile kullanıcı adı eşit değilse şifre doğruysa Kullanıcı Adınız Hatalı yazdırır ve while başına döner eğer şifrede hatalıysa 44.satırdaki koda gider ordaki else çalışır ve Kullanıcı Adı Ve Şifresi Hatalı. yazdırır
        print("Kullanıcı Adınız Hatalı")

    
    
    
    elif ig_ka == kullanıcı_adı and ig_ps != kullanıcı_ps:
        # eğer kullanıcı adı doğru şifre yanlışsa != şifre değişme komutları yazdırılır
        print("Şifreniz Hatalı...")
        print("Şifreniz Değiştirilsin Mi? E/H")
        cevap= input() #cevap input içine gelir
        
        
        
        if cevap=="e":
            #eğer cevap e ise şifre değişme için aşağıdan devam eder
            #eğer cevap h ise while döngüsünün başına dönüp tekrar kullanıcı adı istenir
            print("Şifreniz Değiştiriliyor...")
            yeni_şifre = int(input("Lütfen Yeni Şifrenizi Yazınız : "))
            ig_ps = yeni_şifre # eğer yeni şifre ile girilen şifre eşleşiyorsa if komutuna 14.satıra döner ve hoşgeldiniz komutu çalışır
    
    
    
    else:
        print("Kullanıcı Adı Ve Şifresi Hatalı. ")


    