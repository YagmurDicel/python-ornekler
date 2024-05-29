#Soru 1
print("Merhaba Dünya")

#Soru 2
kullaniciAdi = "Yagmur"
print("Merhaba",kullaniciAdi)

#Soru 3
number1 = 10
number2 = 5
total = number1 + number2
print("Total: ",total)

# Soru 4
sayi1 = float(input("1.Sayı: "))
sayi2 = float(input("2.Sayı: "))
ortalama=(sayi1+sayi2)/2
print(ortalama)

# Soru 5
vize = int(input("Vize Notu: "))
final = int(input("Final Notu: "))
ortalama = (vize*0.4)+(final*0.6)
print(ortalama)

# Soru 6
sınav1 = int(input("1.Sınav Notu: "))
sınav2 = int(input("2.Sınav Notu: "))
sınav3 = int(input("3.Sınav Notu: "))
ortalama = (sınav1+sınav2+sınav3)/3
print(ortalama)

# Soru 7
vize = int(input("Vize Notu: "))
final = int(input("Final Notu: "))
başarıNotu= (vize*0.4)+(final*0.6)
print("Başarı Notunuz: ", başarıNotu)
if(başarıNotu>50):
    print("Tebrrikler...Geçtiniz")
else:
    print("Kaldınız...")

# Soru 8
sayi = 5
if(sayi%2==0):
    print("Sayı çifttir.")
else:
    print("Sayı tektir.")

# Soru 9
number = int(input("Sayıyı Giriniz: "))
if(number>0):
    print("Sayı pozitiftir.")
elif(number<0):
    print("Sayı negatiftir.")
else:
    print("Sayı sıfırdır.")

# Soru 10
kg = float(input("Kilonuz: "))
hg = float(input("Boyunuz: "))
index = (kg/(hg)**2)
