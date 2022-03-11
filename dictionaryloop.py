adict = {"chap1":10 ,"chap2":20  , "chap3":30}


# display only keys
for key in adict.keys():
    print(key)

# display only keys
for key in adict:
    print(key)


# display values only
for value in adict.values():
    print(value)


# display both key:value
for key,value in adict.items():
    print(key,value)
