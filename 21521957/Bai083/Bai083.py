import math

def calculate_S(x, n):
    total = sum(math.sin(x**i) for i in range(1, n+1))
    return total


x = float(input("x: "))
n = int(input("n: "))

result = calculate_S(x, n)
print(f"S({x}, {n}) = {result}")
