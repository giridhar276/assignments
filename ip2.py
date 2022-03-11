'''
Write a Python program to display the below IP addresses

192.168.0.1
192.168.0.2
192.168.0.3
..
..
192.168.0.10
192.168.1.1
192.168.1.2
192.168.1.3
..
..
192.168.1.10
'''

fixed = "192.168."
for val in range(0,2):
    ip = fixed + str(val)
    for val in range(1,11):
        finalip = ip + "." + str(val)
        print(finalip)








    

