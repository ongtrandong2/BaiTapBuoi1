

import math
def calculate_sum(x, n):
    if n <= 0:
        print("n phai la so nguyen duong")
        return None
    total_sum = 0
    for i in range(n+1):
        term = (-1)**i * (x**i) / math.factorial(i)
        total_sum += term
    return total_sum
x = float(input("Nhap x: "))
n = int(input("Nhap n: "))
sum_result = calculate_sum(x, n)
if sum_result is not None:
    print("Tong cua day: ", sum_result)