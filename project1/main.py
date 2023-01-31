x = int(input("Bir sayı giriniz"))
while x < 1:
    if x < 0:
        print("Sayı negatif, lütfen pozitif bir sayı giriniz")
    if x==0:
        print("sayı sıfırdır pozitif gir")
    x = int(input("Bir sayı giriniz:"))
print("Sayınız pozitif ve", x)
