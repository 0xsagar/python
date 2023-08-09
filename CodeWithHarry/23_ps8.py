# Q1: Function to find the greatest of three numbers
# def greatest(n1, n2, n3):
#     if n1 >= n2:
#         if n1 >= n3:
#             return n1
#         else:
#             return n3
#     if n2 >= n1:
#         if n3 >= n2:
#             return n3
#         else:
#             return n2

# print(greatest(3,1,2))

# Q2: Convert Fahrenheit to Celcius
# def celToFah(cel):
#     return cel*(9/5)+32

# print(celToFah(37)) 

# Q3: How do you prevent a new line to be printed
# print("Sagar", end="")
# print("Sagar", end="")

# Q4: Write a recursive function to calculate the sum of n natural numbers
# def sum(n):
#     if n <= 1:
#         return 1
#     return n+sum(n-1)

# print(sum(5))

# Q5: Right angle triangle pattern
# n = 5
# for i in range(n):
#     print("*"*(n-i))


# Q6: Function which converts inches to cms
# def inchesToCms(inches):
#     return inches * 2.54

# print("Cms: ", inchesToCms(12))

# Q7: Remove a given word and strip the string
# this = "     This is a string     "
# print(this)
# print(this.strip())

# def remove_and_strip(word, string):
#     newStr = string.replace(word, "")
#     return newStr.strip()
    
# string = "     Sagar is camping!      "
# print(remove_and_strip("Sagar", string))

# Q8: Write a function to print the multiplication table of a given number
# def multiplication_table(number, i):
    # for x in range(1, 11):
    #     print(f"{number} x {x} = {number*x}")
        # print(str(number) + " x " + str(x) + " = " + str(number*x))

#     if i > 10:
#         return
#     print(f"{number} x {i} = {number*i}")
#     return multiplication_table(number, i + 1)

# print(multiplication_table(5, 1))

