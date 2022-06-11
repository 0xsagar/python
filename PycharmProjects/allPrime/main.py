N = int(input("Print all prime numbers till: "))
for num in range(2, N):
    if N % num == 0:
        continue
    else:
        print(num)