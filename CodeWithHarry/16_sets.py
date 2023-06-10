a = {1, 2, 3, 4, 1}

print(type(a), a)
print(a)
# Set is a collecion of non-repetetive items
# Sets do not have/print  repetetive items

# Important : This empty shows a dict and not a set
b = {}
print(type(b))


#How to initialize an empty set
c = set()
c.add(4)
c.add(5)
c.add(6)
print(type(c), c)

#We can add tuples inside a set but not lists and dictionary
c.add((1,2))
print(c)

#NOTE: We cannot change items inside a set
#NOTE: We cannot change the set by adding the same item multiple times as it'll only be counted once

print(len(c))

c.remove(6) #Removes 6 from the set
c.remove(12) #Throws an error as 12 is not available in the set
print(c)