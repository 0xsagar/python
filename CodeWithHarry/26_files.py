# Read in a file
# f = open('/home/kali/Programming/python/CodeWithHarry/sample.txt', 'r')
# f = open('/home/kali/Programming/python/CodeWithHarry/sample.txt') # Default vault will be set to = read 'r'
# data = f.read()
# data = f.read(5) # Reads first 5 characters
# data = f.readline() # Reads the first line
# print(data)
# data = f.readline() # if written 2nd time, will read the 2nd line
# print(data)
# f.close()

# Write in a file
# f = open("another.txt", "w")
# f.write("This is how you can write in that file")
# If the file is not present, the code will create a new file, if ran multiple times, it will overwrite that file

# Append into that file
f = open("another.txt", "a")
f.write("I an appending into that file")
f.close()
# Now this text will be appended into that another.txt file, if ran multiple times, it will paste the same text at the end multiple times

# The best way to open and close a file is using the 'with' statement (Here we don't need to write f.close, it'll be closed autimatically)
with open("another.txt", "r") as f:
    a = f.read()
with open("another.txt", "w") as f:
    a = f.write("Hello")
print(a)
