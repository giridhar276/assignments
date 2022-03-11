#Write a Python program to display the below IP addresses



'''
192.168.0.1
192.168.0.2
192.168.0.3
..
..
192.168.0.10
'''


fixed =  "192.168.0."
for val in range(1,11):
    ip = fixed + str(val)
    print(ip)
