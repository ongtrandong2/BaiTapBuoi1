def calculate_S(n):
    total = 0
    i = 1
    while True:
        term = 1/i
        total += term
        if term < 10**-6:
            break
        i += 1
    return total


n = int(input("n: "))


result = calculate_S(n)
print(f"S({n}) = {result:.6f}")
