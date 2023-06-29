#Q8: Print the list 
# list = ['banana', 'mango', 'watermelon', 'papaya', 'orange', 'apple']
# i = 0
# # # Using while loop
# while i < len(list):
#     print(list[i])
#     i = i + 1

# ## Using for loop
# for fruit in list:
#     print(fruit)


##Range in for loop: range(start, stop, step_size), here range is [start, stop)
#will print every number from [1,8)
# for x in range(1,8):
#     print(x)
# #will print every number from [1,8)
# for x in range(1,8,1):
#     print(x)

# #will print every 2nd number from [1,8)
# for x in range(1,8,2):
#     print(x)

## Else with for loop
for x in range(10):
    print(x)
    # if x == 5:
    #     break
else:
    print("This is inside the for loop and will be executed after the for-loop has successfully exhausted, won't be shown if loop terminated by break statement")
