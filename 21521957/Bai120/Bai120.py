
import math

def calculate_sequence_term(a, n):
    if n < 1:
        return None

    if n == 1:
        return a

    term = a
    for i in range(2, n + 1):
        term = 5 * term + math.sqrt(24 * term**2 - 8)

    return term

a = int(input("nhap a: "))
n = int(input("nhap  n: "))

result = calculate_sequence_term(a, n)
if result is None:
    print("a hoac n khong hop le")
else:
    print("so hang thu", n, "cua day:", result)