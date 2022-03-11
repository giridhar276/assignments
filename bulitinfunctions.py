print("hello python")
alist = [10,20,30]
print(len(alist))
name  = "python"
print(len(name))

print(list(range(1,11)))
print(list(range(1,11,2)))

value = input()
print("you entered :", value)
      
value = input("Enter any value :")
print("you entered :", value)

alist= [45,34,56,32]
print(max(alist))
print(min(alist))
print(sum(alist))

print(chr(97)) # ascii to char
print(ord('a'))# char to ascii

print(type(alist))  # list
print(isinstance(alist,list))  # True
print(isinstance(alist,tuple))  # False
# converting from list to tuple
atup = tuple(alist)  # typecasting function
print(atup)
svalue = "10"  
val = int(svalue)  # typecasting function
print(type(val))  # integer
