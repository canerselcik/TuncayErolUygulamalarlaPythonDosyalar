ağırlık =int(input("Vücut Ağırlığınızı Giriniz (kg) : "))
boy = float(input("Boy Uzunluğunuzu Giriniz (m): "))

boyhesabı = boy*boy

vki = ağırlık/boyhesabı

print("*"*72)
if vki<= 18.5:
    print("Zayıf : Vücut Kitle İndeksiniz (kg/m²) " , vki)


elif 18.5<=vki<= 24.9:
    print("Sağlıklı : Vücut Kitle İndeksiniz (kg/m²) " , vki)

elif 25<=vki<= 29.9:
    print("Şişman : Vücut Kitle İndeksiniz (kg/m²) " , vki)

elif 30<=vki<= 39:
    print("Obez : Vücut Kitle İndeksiniz (kg/m²) " , vki)

else:

    print("Aşırı Obez (Morbid Obez) : Vücut Kitle İndeksiniz (kg/m²) " , vki)
print("*"*72)