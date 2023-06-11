#Q1: Write a program to create a dict of hindi words and display their meaning when user ask for it?
# myDict = {
#     "pankha" : "fan",
#     "dabba" : "box",
#     "gamla" : "pot",
#     "khidki" : "window"
# }

# print("Options are: ", myDict.keys())
# a = input("What do you want to search in the dictionary: ")
# # print(f"The english translation of {a} is: ", myDict[a]) # Don't use this as it'll give error when the item is not available

# #Use the following method .get as it'll not give any error
# print(f"The english translation of {a} is: ", myDict.get(a))


#Q2: Write a program to input 8 integers and display inly unique ones
# b = set()
# for x in range(8):
#     b.add(int(input("Enter a number: ")))

# print(b)

#Q3: Can we have 18(num) and "18"(string) in a set?
# c = {18, "18"}
# print(c)
# print(len(c))

#Q4: Find the length of the following?
# d = {20, 20.0, "20"}
# print(len(d))

#Q5: What is it's type?
# e = {}
# print(type(e))

#Q6: Let 4 friends add values to their name(keys) in a dict
# f = {}
# x1 = input("Enter your fav language: ")
# x2 = input("Enter your fav language: ")
# x3 = input("Enter your fav language: ")
# x4 = input("Enter your fav language: ")
# f['sagar'] = x1
# f['kiran'] = x2
# f['sudipta'] = x3
# f['abhishek'] = x4
# print(f)

#Q7: What if two friends have the same name in Q6?
#Ans: The latest value will be considered

#Q8: Can you change the value inside a list written below
# s = {8,7,12, "Harry", [1,2]} #Throws an error as list cannot be stored inside a set only tuples can be stored
# s = {8,7,12, "Harry", (1,2)} 
# print(s)