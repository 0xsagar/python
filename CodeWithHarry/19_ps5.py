#Q1: WAP to find the greatest of 4 numbers entered by a user?
# a = []
# for x in range(4):
#     a.append(int(input("Enter number: ")))
# greatest = -999999
# for x in range(4):
#     if(a[x] > greatest):
#         greatest = a[x]
# print("The greatest number is: ", greatest)

#Q2: Check if a student is pass or fail, min 33% each subject and total 40% is required to pass the class.
# sub1 = int(input("Enter first subject marks: "))
# sub2 = int(input("Enter second subject marks: "))
# sub3 = int(input("Enter third subject marks: "))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("You've failed because you've less then 33% in one or more subjects.")
# elif(sub1+sub2+sub3)/2 < 40:
#     print("You've failed due to less total percentage!")
# else:
#     print("You've passed! Congratulations.")

#Q3: Check the comment for spam message keywords.
# comment = input("Enter your comment: ")
# if("make a lot of money" in comment):
#     spam = True
# elif("buy now" in comment):
#     spam = True
# elif("click this" in comment):
#     spam = True
# elif("subscribe this" in comment):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This comment is spam")
# else:
#     print("This comment is not spam")

#Q4: Check if the username comtain less than 10 characters or not
# username = input("Enter your username: ")
# if(len(username) < 10):
#     print(f"{username} has less than 10 characters.")
# else:
#     print(f"{username} has more than 10 characters")

#Q5: Check is the name si present in the list of not
# list = ["sagar", "kiran", "sudipta", "abhishek"]
# name = input("Enter your name: ")
# if(name in list):
#     print("Your name is present in the list.")
# else:
#     print("Your name is not present in the list")

#Q6: Make a grading system
# marks = int(input("Enter your marks: "))
# if(marks >= 90):
#     grade = "S"
# elif(marks >= 80):
#     grade = "A"
# elif(marks >= 70):
#     grade = "B"
# elif(marks >= 60):
#     grade = "C"
# elif(marks >= 50):
#     grade = "D"
# elif(marks < 50):
#     grade = "F"
# print("Your grade is " + grade)

#Q7: Is this post talking about sagar in any form
# post = "I've known sagAR from many years"
# name = "SAGAr"
# if(name.lower() in post.lower()):
#     print("Yes this post is talking about sagar!")
# else:
#     print("No, this post isn't talking about sagar")


