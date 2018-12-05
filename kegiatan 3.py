import shelve
hiya3=shelve.open('L200184165.data', 'r')
for i in hiya3 ['data']:
    print(i)
hiya3.close()
