import subprocess as sp

'''
sp.call("C:\Program Files\Google\Chrome\Application\chrome.exe")
# İçine Yazılan Yollu exe yi açar
'''
psw = "727272"
kullanıcı_şifre = input("Uygulamaya Erişmek İçin Şifrenizi Giriniz : ")

if kullanıcı_şifre == psw:
    while True:
        print("***UYGULAMA AÇMA EKRANINA HOŞGELDİNİZ***")

        seçim_yap = input("1-Notepad\n2-Google\n3-Hesap Makinesi\n")
        
        if seçim_yap =="1":
            sp.call("notepad.exe")
            input("Devam Edilsin mi?")
        elif seçim_yap =="2":
            sp.call("C:\Program Files\Google\Chrome\Application\chrome.exe")
            input("Devam Edilsin mi?")
        elif seçim_yap =="3":
            sp.call("calc.exe")
            input("Devam Edilsin mi?")
        
        