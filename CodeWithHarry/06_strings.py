a = 24
b = "Harry"
print(a, b)
print(type(a))
print(type(b))

# triple quote string is used to store double and single quote letters inside it
# eg - '''Sagar's height is 5"7 '''

# Concatenating two strings
name = "Sagar"
print(name[0])

# String Slicing
# it'll print from index 0 to n-1 (eg - [0:3] includes 0, 1 and 2)
print(name[0:3])
print(name[:4])  # empty initial index means the beginning
print(name[0:])  # enpty final index means till the end
print(name[1:])  # is same as name[1:4]
c = name[-4:-1]  # is same as name[1:4] --> Use the drawing method to find accutate explaination
print(c)

# skipping and slicing strings
print()
word = "SagarIsGood"
d = word[0::2]  # select from 0 to end and skip every 2nd letter
print(d)
