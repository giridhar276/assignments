adict = {"chap1":10 ,"chap2":20  , "chap1":1000}
print(adict)
#adding new key:value pair
adict["chap3"] = 30
adict["chap4"] = 40
print(adict)
print(adict)


# only keys
print(adict.keys())
print(list(adict.keys()))

# only values
print(list(adict.values()))

# keys:value pairs
print(list(adict.items()))

#print(adict["chap5"])
print(adict.get("chap5"))
print(adict.get("chap1"))

adict.pop("chap1")
print("after deleting :", adict)

adict.popitem()
print("after popitem :", adict)


adict = {"chap1":10 ,"chap2":20  , "chap1":1000}
bdict = {"chap8":80,"chap9":90,"chap1":2000}

print(adict.update(bdict))

print(adict)
print(bdict)




































