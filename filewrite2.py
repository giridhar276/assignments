'''
## write operation
# regular approach
# traditional way
fobj = open("languages.txt","w") 
fobj.write("python programming\n")
fobj.write("scala programming\n")

fobj.close()
'''


# context manager
# modern approach or pythonic way
# file will be closed automatically
#when it comes out of context ... file gets closed automatically
with open("info.txt","w")  as fobj:
    fobj.write("python programming\n")
    fobj.write("scala programming\n")


    

