from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"Turkish_Turkey.1254")

# %a hafta gününün kısaltılmış hali
# %A hafta gününün tam adı
# %b ayın kısaltılmış adı
# %B ayın tam adı
# %c tam tarih, saat ve zaman bilgisi
# %d sayı değerli bir karakter dizisi olarak gün
# %j belli bir tarihin, yılın kaçıncı gününe denk geldiğini gösteren 1-366 arası bir sayı
# %m sayı değerli bir karakter dizisi olarak ay

a = datetime.now()

tam_tarih = datetime.strftime(a,"%m")



print(tam_tarih)


