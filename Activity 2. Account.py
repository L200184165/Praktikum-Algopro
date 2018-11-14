## Program Akun
## Dibuat Oleh David L20000012
import random
angka_random = random.randint(0,1000)
Nama = 'Muhammad Irfan'
TanggalLahir='13 Juli 2000'
Nama_Singkat = Nama[0] +'.'+ Nama[9:14] 
Username = Nama[0]+TanggalLahir[0:2]+TanggalLahir[8:13]
Password = Nama[0:3]+str(angka_random)

