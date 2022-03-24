myDict = {
    "fast": "In a quick manner",
    "sagar": "A Hacker",
    "marks": [1, 2, 3],
    "newDict": {'harry': 'youtube'}  # dictionary inside dictionary
}

print(myDict)
print(myDict["sagar"])
myDict["marks"] = [21, 45]  # values can be changed
print(myDict["newDict"]["harry"])  # nested dictionary
