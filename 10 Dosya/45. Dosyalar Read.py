import codecs # Türkçe karakter sorunu için

with codecs.open("c:/Users/Windows 10/Desktop/ /Python/10 Dosya/deneme.txt", "r", encoding="utf-8") as dosya: # dosya.txt dosyasını okuma modunda aç
      '''
      a = dosya.readline() # dosyayı satır satır oku ve a değişkenine ata
      print(a)
      '''
      '''
      birinci = dosya.readline() # dosyayı satır satır oku ve birinci değişkenine ata
      ikinci = dosya.readline()

      print(birinci+ikinci) # iki satırı birleştirerek ekrana yazdır

      # kanuni ve abdulhamit olaarak çıkar
      '''
      '''
      a = dosya.readlines() # dosyayı satır satır oku ve a değişkenine ata  
      # dosyayı satır satır okuyup bir listeye atar index yani 0-1-2 olur 
      
      print(a) # dosyanın tüm satırlarını ekrana yazdır
      say = 1
      for i in a: # a değişkenindeki tüm satırları i değişkenine ata
            print(say,":",i)
            say+=1
      '''

      a = dosya.readlines()

      print(a[0]) # dosyanın ilk satırını ekrana yazdır

     
