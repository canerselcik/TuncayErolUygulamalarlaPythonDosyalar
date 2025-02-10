
'''
dosya = open("deneme.txt","w") # bu yola bakar eğer deneme.txt varsa açar yoksa w ile oluşturur.

dosya.write("Merhaba Dünya") # dosyaya yazma işlemi yapar.


'''
#---------------------------------------------------------
'''
dosya = open("deneme.txt","a") # bu dosyaya w gibi değilde veri ekle veriyi silmez

dosya.write("Merhaba Dünya")

'''
#------------------------------------------------------

dosya = open("deneme.txt","r") # dosyayı okuma işlemi yapar.

a = dosya.read() # dosyadaki veriyi okur.

print(a)