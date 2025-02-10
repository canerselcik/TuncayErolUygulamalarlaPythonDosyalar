# Sözlükler kısa anlamda dizeler gibidir. dizeler gibiiçine birden fazla eleman alır

#sözlüklerde ikili değer vardır. sözlük oluşturunca bir isim veririz ve o isme bir değer veririz   apple : elma 

'''
sözlük = {"Apple":"Elma"} # sözlüğe ismi apple olan anlamı elma olan bir hazne ekledik ikisi tek bir veri bloğunu ifade ediyor

print(sözlük["Apple"]) # burda sözlüğün içindeki ismi çağırıyoruz bunun karşılığında bize ismin değeri yani çıktımız elma olarak gelecektir

'''

#------------------------------------------------------------------------------------

'''

sözlük = {"Apple":"Elma","İsim":"Emir","Telefon":"Samsung"} # her virgül bir elementtir. virgüller sözlükleri birer birer birbirinden ayırır.

print(sözlük["Telefon"])

'''

#------------------------------------------------------------------------------------

sözlük = {"Apple":"Elma","İsim":"Emir","Telefon":"Samsung"}

for isim,deger in sözlük.items(): # items yani sözlüğün içindeki bütün elementler  bu sayede sözlüğün içindeki ikili değerleri yazdırırız
    print(isim,":",deger)