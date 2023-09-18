def calculate_S(n, k):
    total = sum(i**k for i in range(1, n+1))
    return total


n = int(input("n: "))
k = int(input("k: "))


result = calculate_S(n, k)
print(f"S({n}, {k}) = {result}")

