import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50001))
s.listen(5)
print "Server sudah siap"
data = ''
kamus = {'nama':'Muhammad Irfan',
         'NIM':'L200184165',
         'angkatan':'2018',
         'keluar':'Asiap!!'}
while data.lower() != 'keluar':
    komm, addr = s.accept()
    while data.lower() != 'keluar':
        data = komm.recv(1024)
        print 'Perintah: ',data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Maaf, perintah tidak dimengerti')
