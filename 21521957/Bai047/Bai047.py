import math

def calculate_sum(m):
    total = 0
    for n in range(1, m):
        total += math.sqrt(1 + 1/(n**2) + 1/((n+1)**2))
    return total


m = int(input("Nhap m: "))


result = calculate_sum(m)
print(f"Tong: {result:.4f}")
