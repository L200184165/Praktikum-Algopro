hiya = open("L200184165.txt", "r")
NIM = hiya.readline()
TTL = hiya.readline()
Nama = hiya.readline()
hiya.close()

import shelve
hiya2 = shelve.open('L200184165.data')
hiya2['data'] = [NIM, TTL, Nama]
hiya2.close()
