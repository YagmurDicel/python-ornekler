# Soru 41
sayi1=float(input("Birinci sayıyı girin: "))
sayi2=float(input("İkinci sayıyı girin: "))
if sayi1 < 0 and sayi2 > 0:
    negatif = sayi1
    pozitif = sayi2
elif sayi1 > 0 and sayi2 < 0:
    negatif = sayi2
    pozitif = sayi1
else:
print("Lütfen bir sayıyı negatif, diğerini pozitif girin.")
exit()
print("Mutlak değerler:")
print(abs(negatif))
print(abs(pozitif))
# Soru 42
liste=[5, 8, 12, 4, 6]
toplam = 0
ogelerin_sayisi = 0
for eleman in liste:
    toplam += eleman
    ogelerin_sayisi += 1
    ortalama = toplam / ogelerin_sayisi
print("Liste öğelerinin ortalaması:", ortalama)
# Soru 43
liste=[5, 8, 12, 4, 6]
toplam = 0
ogelerin_sayisi = 0
while liste:
    eleman = liste.pop()
    toplam += eleman
    ogelerin_sayisi += 1
    ortalama = toplam / ogelerin_sayisi
    print("Liste öğelerinin ortalaması:", ortalama)
    print("Listede toplam", ogelerin_sayisi, "eleman bulunuyor.")
# Soru 44
sayi=int(input("Sayı Giriniz: "))
toplam=i
for i in range(sayi,0,-1):
    toplam *= i
    print("sonuc=",toplam)
# Soru 45
fahrenheit=float(input("Fahrenheit derecesini girin: "))
celsius = (fahrenheit - 32) * 5/9
print("Girdiğiniz Fahrenheit derecesinin Celsius karşılığı:", celsius)
# Soru 46
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
delta = b**2-4*a*c
x1=(-b+ delta**0.5)/2*a
x2=(-b- delta**0.5)/2*a
print("denklemimizin kökleri {} ve {}'dir'".format(x1,x2))
if (delta>0):
    print("2 farklı reel kök var.")
elif (delta==0):
    print("Çift katlı reel kök")
else:
    print("Reel kök yok.")
# Soru 47
#BOŞ
# Soru 48
a=12
h=8
üçgeninalanı=a*h/2
print(üçgeninalanı)
# Soru 49
sayi =float(input("Bir sayı girin: "))
if sayi > 0:
print("Girdiğiniz sayı pozitif.")
elif sayi < 0:
print("Girdiğiniz sayı negatif.")
else:
print("Girdiğiniz sayı sıfır.")
# Soru 50
#Boş
