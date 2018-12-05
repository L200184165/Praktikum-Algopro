import shelve
hiya4 = shelve.open('L200184165.data', 'r')
for i in hiya4 ['data']:
    print (i)
hiya4.close()
