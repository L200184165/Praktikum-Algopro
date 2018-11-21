a = ('Irfan')
d=0
while d<3:
    b = input('masukkan password:')
    if b == a:
        print('anda berhasil login')
        break
    elif b != a:
        print('maaf, anda salah memasukkan password.  ')
        d=d+1
if d==3:
    print('maaf anda telah mencoba 3 kali, akses anda di tolak')
