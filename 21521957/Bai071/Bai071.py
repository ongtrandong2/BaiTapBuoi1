def calculate_S(x, n):
    total = 0
    for i in range(n+1):
        total += x**(2*i + 1)
    return total


x = float(input("x: "))
n = int(input("n: "))


result = calculate_S(x, n)
print(f"S({x}, {n}) = {result}")
