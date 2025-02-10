
vize_notu = int(input("Vize Notunuzu Giriniz : "))
final_notu = int(input("Final Notunuzu Giriniz : "))

ortalama_al = (final_notu+vize_notu)/2

print("*"*72)
if ortalama_al>=85:
    print("Tebrikler AA Aldınız : Ortalamanız" , ortalama_al)


elif ortalama_al>=65:
    print("Tebrikler BB Aldınız : Ortalamanız" , ortalama_al)

elif ortalama_al>=50:
    print("Tebrikler CC Aldınız : Ortalamanız" , ortalama_al)

else: 
    print("Malesef Dersten Kaldınız : Ortalamanız" , ortalama_al)

print("*"*72)