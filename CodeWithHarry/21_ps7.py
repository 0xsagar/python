# Q1: Write a for loop to write multiplication table of any given number
# number = int(input("Give a number: "))
# for x in range(1, 11):
#     print(f"{number} x {x} = {number*x}")
#     print(str(number) + " x " + str(x) + " = " + str(number*x))

# Q2: WAP to greet all the persons whose name starts with "S" in the given list
# l1 = ["Harry", "Sagar", "Sudipta", "Abhishek"]
# for name in l1:
#     if name.startswith("S"):
#         print(f"Good Morning {name}")

# Q3: Solve Q1 using while loop
# i = 1
# number = int(input("Give a number: "))
# while i <= 10:
#     print(f"{number} x {i} = {number*i}")
#     i+=1

# Q4: WAP to find whether a number is prime or not
# number = int(input("Give a number: "))
# prime = True
# for i in range(2, number):
#     if (number % i == 0):
#         prime = False
#         break
# if prime == False:
#     print("The number is not Prime")
# if prime == True:
#     print("The number is Prime")

# Q5: WAP to find the sum of first n natural numbers using while loop
# number = int(input("Give a number: "))
# i = 0
# sum = 0
# while i <= number:
#     sum += i
#     i += 1
# print(sum)

# Q6: WAP to find factorial using for loop
# number = int(input("Give a number: "))
# factorial = 1
# for x in range(1, number+1):
#     factorial *= x
# print("factorial =", factorial)
# print(f"The factorial of {number} is {factorial}")

# Q7: Print right angle triangle pattern
# number = int(input("Give a number: "))
# for x in range(number):
#     print("*" * (x+1))

# Q8: Print pyramid pattern
# number = int(input("Give a number: "))
# for x in range(number):
#     print(" " * (number - x - 1), end = "")
#     print("*" * (2*x+1), end = "")
#     print(" " * (number - x - 1))

# Q9: Write empty box pattern
number = int(input("Give a number: "))
for i in range(number):
    for j in range(number):
        print("x", end="")
    print("")







