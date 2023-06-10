myDict = {
    "fast": "In a quick manner",
    "sagar": "A Hacker",
    "marks": [1, 2, 3],
    "newDict": {'harry': 'youtube'},  # dictionary inside dictionary
    1: 2
}

print(myDict.keys())  # print keys
print(list(myDict.keys()))  # print keys in list format

print(myDict.values())  # print values
print(myDict.items())  # prints the (key, value) pair

print(myDict.get("sagar"))  # prints the value of key "sagar"
print(myDict["sagar"])  # prints the value of key "sagar"

# # The difference between .get and [] syntax in dictionaries
# print(myDict.get("sagar2"))  # returns None as sagar2 is not present in the key
# print(myDict["sagar2"])  # Returns an error as sagar2 is not present in the key


print(myDict)
updateDict = {
    "sagar2" : "software engineer",
    "age" : 21,
    "fast": "extremely"
}
myDict.update(updateDict) #Updates the dictionary by adding the new key-value pairs from updateDict
print(myDict)