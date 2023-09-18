
import math
def calculate_sequence(n):
    if n < 1:
        return None

    total = 0.0
    for i in range(n, 0, -1):
        factorial = math.factorial(i)
        sqrt_factorial = math.sqrt(factorial)
        total += sqrt_factorial

    return total

n = int(input("Nhap n: "))

result = calculate_sequence(n)
if result is None:
    print("n khong dat yeu cau")
else:
    print("ket qua: ", result)