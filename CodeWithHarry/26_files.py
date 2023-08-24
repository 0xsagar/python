# f = open('/home/kali/Programming/python/CodeWithHarry/sample.txt', 'r')
f = open('/home/kali/Programming/python/CodeWithHarry/sample.txt') # Default vault will be set to = read 'r'
# data = f.read()
# data = f.read(5) # Reads first 5 characters
data = f.readline() # Reads the first line
print(data)
data = f.readline() # if written 2nd time, will read the 2nd line
print(data)
f.close()