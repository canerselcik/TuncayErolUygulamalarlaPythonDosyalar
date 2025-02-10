import time


try:
    sayı1= int(input("Sayı1:"))
    sayı2= int(input("Sayı2:"))

    toplam = sayı1+sayı2

    print(toplam)

except ValueError:
  print("Lütfen Sayı Giriniz")


finally:
   sayaç = 5

   for i in range(5):
      time.sleep(1)
      print("Geri Sayım :",sayaç)
      sayaç-=1
      if sayaç == 0:
         print("Bomba Patladı :)))")