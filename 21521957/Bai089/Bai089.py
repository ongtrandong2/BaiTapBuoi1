def calculate_S(x, n):
    total = 0
    denominator = 0
    
    for i in range(1, n+1):
        denominator += i
        total += ((-1)**i) * (x**i) / denominator
    
    return total


x = float(input("x: "))
n = int(input("n: "))

result = calculate_S(x, n)
print(f"S({x}, {n}) = {result}")
