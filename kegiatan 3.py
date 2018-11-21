a = input('Masukkan Nama Saudara : ')
b = float(input('Pukul Berapa Sekarang : '))
if 00.00 <= b <= 03.59:
    b = "Petang"
elif 04.00 <= b <= 11.59:
    b = "Pagi" 
elif 12.00 <= b <= 14.59 :
    b = "Siang"
elif 15.00 <= b <= 17.59 :
    b = "Sore"
elif 18.00 <= b <= 23.59 :
    b = "Malam"
print("Selamat " + b + " " + a)

