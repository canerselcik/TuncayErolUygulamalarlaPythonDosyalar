
import codecs # Türkçe karakter sorunu için
'''
with codecs.open("c:/Users/Windows 10/Desktop/ /Python/10 Dosya/deneme.txt", "a", encoding="utf-8") as dosya: # "a" dosyanın sonuna ekleme yapar sadece

    dosya.write("\n2.Mahmut") # Dosyaya sonuna ekleme yapar
'''
'''
with codecs.open("c:/Users/Windows 10/Desktop/ /Python/10 Dosya/deneme.txt", "r+", encoding="utf-8") as dosya: # "r+" hem okuma hem yazma yapar
    
    db = dosya.read() 
    dosya.seek(0) # Dosyanın başına git
    db = "3.Emin\n" + db # Dosyanın başına ekleme yap

    dosya.write(db) # Dosyaya yazdır
'''
with codecs.open("c:/Users/Windows 10/Desktop/ /Python/10 Dosya/deneme.txt", "r+", encoding="utf-8") as dosya: 
    
    db = dosya.readlines() # Dosyayı satır satır oku
    db.insert(2,"Antep\n")# Dosyanın 2. satırına ekleme yap
    dosya.seek(0) # Dosyanın başına git baytlar arasında gezinme yapar
    dosya.writelines(db) # Dosyaya yazdır