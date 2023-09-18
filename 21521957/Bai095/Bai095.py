import math

def calculate_S(n):
    result = math.sqrt(n)
    for i in range(n-1, 0, -1):
        result = math.sqrt(i + result)
    return result


n = int(input("n: "))


result = calculate_S(n)
print(f"S({n}) = {result}")
