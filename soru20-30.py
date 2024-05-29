# Soru 21
tercih = input("Tercihiniz sinema ise 'sinema', tiyatro ise 'tiyatro' yazınız: ")
ogrenci_mi = input("Öğrenci misiniz? (evet/hayır): ")
sinema_fiyati = 49.50
tiyatro_fiyati = 29.80
indirimli_fiyat = 0.50
if (tercih == 'sinema'):
    odenecek_tutar = indirimli_fiyat(sinema_fiyati, ogrenci_mi == 'evet')
elif (tercih == 'tiyatro'):
    odenecek_tutar = indirimli_fiyat(tiyatro_fiyati, ogrenci_mi == 'evet')
# Soru 22
x = 55
if (x==2):
    print("Sayı asaldır.")
elif (x%2==0):
    print("Sayı asaldır.")
else:
    print("Sayı asal değildir.")
# Soru 23
n = input("Bir Sayı Giriniz: ")
tek_toplam = 0
cift_toplam = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        cift_toplam += i
    else:
        tek_toplam += i
    print(f"1'den {n}'e kadar olan tek sayıların toplamı: {tek_toplam}")
    print(f"1'den {n}'e kadar olan çift sayıların toplamı: {cift_toplam}")
# Soru 24
maas = float(input("Mevcut maaşınızı girin: "))
zam_orani = float(input("Zam oranını yüzde olarak girin (örneğin, %10 zam için 10 girin): "))
zam_miktari = maas * (zam_orani / 100)
zamli_maas = maas + zam_miktari
print(f"Zam miktarı: {zam_miktari:.2f} TL")
print(f"Zamlı maaşınız: {zamli_maas:.2f} TL")
# Soru 25
pi = 3.14
r = 6
alan = pi*r*r
print(alan)
# Soru 26
random_number = random.randint(1, 100)
sayac=0
guess = int(input("Bir sayı tahmin edin (1-100): "))
sayac+=1
if guess == random_number:
    print(f"Tebrikler! Doğru tahmini yaptınız. Sayı: {random_number}, Deneme sayısı: {sayac}")
elif guess < random_number:
    print("Daha büyük bir sayı tahmin edin.")
else:
    print("Daha küçük bir sayı tahmin edin.")
# Soru 27
#BOŞ
# Soru 28
liste = [2, 5, 10, 15, 20, 25, 30, 35, 40, 45]
besin_katlari = [sayi for sayi in liste if sayi % 5 == 0]
print("5'in katları:", besin_katlari)
# Soru 29
onceden_tanimlanmis_string ="Bu bir önceden tanımlanmış string."
girdi=input("Aramak istediğiniz stringi girin: ")
if girdi in onceden_tanimlanmis_string:
    print("Girdi önceden tanımlanmış string içinde bulunuyor.")
else:
    print("Girdi önceden tanımlanmış string içinde bulunmuyor.")
# Soru 30
sayi1=int(input("Birinci sayıyı girin: "))
sayi2=int(input("İkinci sayıyı girin: "))
if sayi1 > sayi2:
    sayi1, sayi2 = sayi2, sayi1
    toplam_cift_sayilar =0
    cift_sayi_adedi =0
    for i in range(sayi1, sayi2 + 1):
if i % 2 == 0:
     toplam_cift_sayilar += i
     cift_sayi_adedi +=1
if cift_sayi_adedi != 0:
     ortalama = toplam_cift_sayilar / cift_sayi_adedi
print("Girdiğiniz iki sayı arasındaki çift sayıların ortalaması:", ortalama)
else:
print("Girdiğiniz aralıkta çift sayı bulunmamaktadır."),
