
import math
def calculate_S(x, n):
    if n <= 0:
        print("n phai la so nguyen duong")
        return None

    if abs(x) > 1:
        print("x khong dat yeu cau")
        return None

    result = 0
    for _ in range(n):
        result = math.sin(result + x)
    return result
x = float(input("Nhap x: "))
n = int(input("Nhap n: "))
S = calculate_S(x, n)
if S is not None:
    print("Tong cua day la:", S)
