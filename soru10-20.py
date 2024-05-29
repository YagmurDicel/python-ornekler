# Soru 10
kg = float(input("Kilonuz: "))
hg = float(input("Boyunuz: "))
index = (kg/(hg)**2)
# Soru 11
yaş = int(input("Yaşınızı Giriniz: "))
if(yaş<18):
    print("Ehliyet Alamazsınız.")
else:
    print("Ehliyet Alabilirsiniz.")
# Soru 12
for i in range(1,101):
    print(i)
# Soru 13
for sayi in range(2, 101, 2):
    print(sayi, end=" ")
# Soru 14
for sayi in range(1, 101, 2):
    print(sayi, end=" ")
# Soru 15
sayi=sayi
for sayi in range(1, 101):
if (sayi % 3 == 0 and sayi % 5 == 0):
    print(sayi, end=" ")
# Soru 16
sayi = sayi
sayi=int(input("Bir sayı girin: "))
for i in range(1, sayi + 1):
    print(i, end=" ")
# Soru 17
kısaKenar = int(input("Kısa Kenar Uzunluğunu Giriniz: "))
uzunKenar = int(input("Uzun Kenar Uzunluğunu Giriniz: "))
alan = (kısaKenar*uzunKenar)
çevre = (kısaKenar+uzunKenar)*2
# Soru 18
pi = 3.14
r = 4
cevre = 2*pi*r
print(cevre)
# Soru 19
a = input("Bir Kelime Giriniz: ")
for kelime in (a):
    print(kelime)
# Soru 20
veri1=input("Lütfen başlangıç için bir sayı giriniz: ")
veri2=input("Lütfen bitiş için bir sayı giriniz: ")
for i  in range (int(veri1),int(veri2)+1) :
