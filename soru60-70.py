# Soru 61
negatif_sayilar = 0
pozitif_sayilar = 0
for i in range(10):
    sayi = int(input(f"{i + 1}. tamsayıyı girin: "))
if sayi < 0:
    negatif_sayilar += 1
elif sayi > 0:
    pozitif_sayilar += 1
    print("Girilen sayılardan", negatif_sayilar, "tanesi negatif.")
    print("Girilen sayılardan", pozitif_sayilar, "tanesi pozitif.")
# Soru 62
kareler_toplami = 0
for sayi in range(1, 26):
    kareler_toplami += sayi ** 2
    print("1'den 25'e kadar olan sayıların karelerinin toplamı:", kareler_toplami)
# Soru 63
r = 5
h = 10
pi = 3
silindirinalanı = (2*pi*r*r)+(2*pi*r*h)
print(silindirinalanı)
silindirinhacmi= pi*r*r*h
print(silindirinhacmi)
# Soru 64
r = 6
pi = 3
küreninalanı= 4*pi*r*r
print(küreninalanı)
küreninhacmi= 4/3/pi*r*r*r
print(küreninhacmi)
# Soru 65
menu = {
    "Kuru Fasulye": 15.99,
    "Tavuk Döner": 30.50,
    "İskender": 24.00,
    "Tarhana Çorbası": 8.99,
    "Pilav": 18.50,
    "Sütlaç": 8.50
}
print("Lokantanın Menüsü:")
for yemek, fiyat in menu.items():

print(f"{yemek}: {fiyat} TL")
# Soru 66
# Soru 67
menu = {
    "Kuru Fasulye": 15.99,
    "Tavuk Döner": 30.50,
    "İskender": 24.00,
    "Tarhana Çorbası": 8.99,
    "Pilav": 18.50,
    "Sütlaç": 8.50
}
print("Lokantanın Menüsü:")
for yemek, fiyat in menu.items():
print(f"{yemek} => {fiyat} TL")
# Soru 68
menu = {
    "Kuru Fasulye": 15.99,
    "Tavuk Döner": 30.50,
    "İskender": 24.00,
    "Tarhana Çorbası": 8.99,
    "Pilav": 18.50,
    "Sütlaç": 8.50
}
yemek=input("Yediğiniz yemeğin adını girin: ")
if yemek in menu:
    fiyat = menu[yemek]
    print(f"{yemek} yemeğinin fiyatı: {fiyat} TL")
# Soru 69
menu = {
    "Kuru Fasulye": 15.99,
    "Tavuk Döner": 30.50,
    "İskender": 24.00,
    "Tarhana Çorbası": 8.99,
    "Pilav": 18.50,
    "Sütlaç": 8.50
}
toplam_borc=0
print("Yemeklerinizi yazın, her bir yemeği yazdıktan sonra ENTER tuşuna basın.")
print("Toplam borcu görmek için '$' tuşuna basın.")
while True:
    yemek = input("Yediğiniz yemeğin adını girin (veya '$' tuşuna basarak çıkın): ")
    if yemek == '$':
break
if yemek in menu:
        toplam_borc += menu[yemek]
print(f"Toplam borcunuz: {toplam_borc:.2f} TL")