def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


n = int(input("nhap n: "))


if n < 0:
    print("so am khong tinh duoc")
else:
    result = factorial(n)
    print(f"{n}! = {result}")

