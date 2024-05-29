# Soru 31
n =int(input("Kaç adet sayı gireceksiniz: "))
tek_toplam =0
tek_adet =0
cift_toplam =0
cift_adet =0
for _ in range(n):
    sayi = int(input("Bir sayı girin: "))
if sayi % 2 == 0:
        cift_toplam += sayi
        cift_adet += 1
else:
        tek_toplam += sayi
        tek_adet += 1
if tek_adet > 0:
        tek_ortalama = tek_toplam / tek_adet
print("Girilen tek sayıların ortalaması:", tek_ortalama)
else:
print("Girilen sayılar arasında tek sayı yok.")
if cift_adet > 0:
    cift_ortalama = cift_toplam / cift_adet
print("Girilen çift sayıların ortalaması:", cift_ortalama)
else:
print("Girilen sayılar arasında çift sayı yok.")
# Soru 32
araba_markalari = ["Mercedes-Benz", "BMW", "Audi"]
print("En sevdiğiniz 3 araba markası:")
for marka in araba_markalari:
print(marka)
# Soru 33
liste = [3, 1, 2]
liste[0] = 1
liste[1] = 1
print(liste)
# Soru 34
tuple_1=(4, 11, 20)
tuple_2=(41, 18, 25)
print("Orijinal tuple:", tuple_1)
print("Yeni tuple:", tuple_2)
# Soru 35
dogumgünü=int(input("Doğum gününüzü (GG/AA/YYYY formatında) girin: "))
yas=int(input("Yaşınızı Giriniz: "))
print(dogumgünü)
print(yas)
# Soru 36
#BOŞ
# Soru 37
sayi=input("Bir sayı girin: ")
toplam = 0
for rakam in sayi:
    toplam += int(rakam)
print("Girdiğiniz sayının rakamlarının toplamı:", toplam)
# Soru 38
metin=input("Bir metin girin: ")
sayi=int(input("Kaç kez yazdırmak istediğinizi girin: "))
for _ in range(sayi):
print(metin)
# Soru 39
metin=input("Bir metin girin: ")
sayi=int(input("Kaç kez yazdırmak istediğinizi girin: "))
sayac = 0
while sayac < sayi:
print(metin)
sayac += 1
# Soru 40
toplam=0
while True:
    sayi = int(input("Bir sayı girin (Çıkmak için 0'a basın): "))
    if sayi == 0:
        break
        toplam += sayi
        print("Girdiğiniz sayıların toplamı:", toplam)
