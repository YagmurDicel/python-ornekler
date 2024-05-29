# Soru 51
#Boş
# Soru 52
toplam=0
for i in range(10):
    sayi = float(input(f"{i+1}. sayıyı girin: "))
    toplam += sayi
print("Girdiğiniz 10 sayının toplamı:", toplam)
# Soru 53
toplam=0
for i in range(10):
 sayi =sayi
float(input(f"{i + 1}. sayıyı girin: "))
toplam += sayi
ortalama = toplam / 10
print("Girdiğiniz 10 sayının toplamı:", toplam)
print("Girdiğiniz 10 sayının ortalaması:", ortalama)
# Soru 54
sayi=[]
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
sayi3 = float(input("Üçüncü sayıyı girin: "))
en_kucuk= sayi[0]
en_buyuk= sayi[0]
if en_kucuk>sayi:
    en_kucuk=sayi
if en_buyuk<sayi:
        en_buyuk=sayi
print("En büyük sayı:", en_buyuk)
print("En küçük sayı:", en_kucuk)
# Soru 55
a = int(input("Birinci sayıyı girin: "))
b = int(input("İkinci sayıyı girin: "))
sayilar = list(range(a, b+1))
print("a ve b arasındaki sayılar:", sayilar)
# Soru 56
mesafe = float(input("Gidilecek mesafeyi km cinsinden girin: "))
ortalamahız=90
sure = mesafe / ortalamahız
print("Aracın belirtilen mesafeyi gitmesi için gereken süre:", sure, "saat")
# Soru 57
toplam = sum([i**2 for i in range(1, 101)])
print("1^2 + 2^2 + 3^2 + ... + 100^2 =", toplam)
# Soru 58
taban=int(input("Taban sayıyı girin: "))
kuvvet=int(input("Kuvvet sayısını girin: "))
sonuc = taban ** kuvvet
print(f"{taban} sayısının {kuvvet}. kuvveti:", sonuc)
# Soru 59
toplam=0
sayac=0
while True:
    sayi=float(input("Bir sayı girin (Negatif sayı girişi durdurur): "))
    if sayi < 0:
        break
    toplam += sayi
    sayac += 1
    if sayac > 0:
        ortalama = toplam / sayac
        print("Girilen sayıların ortalaması:", ortalama)
# Soru 60
#Boş
