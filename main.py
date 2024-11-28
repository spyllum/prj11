import random
degıskenler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Lütfen şifre uzunluğunu giriniz : "))
sifre  = ""
for i in range(uzunluk):
    sifre += random.choice(degıskenler)

print("Oluşturla Şİfre : ", sifre)
