
import math

def calculate_exponential(x, n):
    if n < 0:
        return None

    result = 1.0
    term = 1.0

    for i in range(1, n + 1):
        term *= x / i
        result += term

    return result

x = float(input("nhap x: "))
n = int(input("nhap n: "))

result = calculate_exponential(x, n)
if result is None:
    print("n khong dat yeu cau")
else:
    print("ket qua: %.6f" % result)