N = int(input("Check if this number is prime?: "))
for num in range(2, N):
    if N % num == 0:
        print("Not Prime")
    else:
        print("Prime")
    exit(0)