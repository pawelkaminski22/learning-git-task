sklepy = {
'piekarnia': ['chleb', 'pączek', 'bułki'],
'warzywniak': ['marchew', 'seler', 'rukola'],
'lidl': ['czekolada', 'papier', 'szmpon']
}
count = sum([len(value) for value in sklepy.values()])

for sklep in sklepy:
    print("Idę do", sklep.capitalize() , "i kupuję tam:", ', '.join([s.capitalize() for s in sklepy.get(sklep)]))

print("W sumie kupuję", count, "produktów")
print('drugi commit')

#a = [11,122,12,32,10,43,23,53,123,54,24]
#print(' > '.join([str(ae) for ae in a]))