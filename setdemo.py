

aset =  {10,10,20,20,30,30}
bset = {30,40,50,50,40,30}

print(aset,bset)

# unique values of both a and b
print(aset.union(bset))

# common values
print(aset.intersection(bset))

# issubnet issupernet
print(aset.issubset(bset))
print(aset.issuperset(bset))


aset =  {10,10,20,20,30,30}
aset.add(10)
print("After adding :", aset)
aset.add(70)
print("After adding :", aset)

aset.update(bset)
print(aset)
