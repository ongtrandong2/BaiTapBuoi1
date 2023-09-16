def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a = int(input("a: "))
b = int(input("b: "))


gcd = find_gcd(a, b)
print(f"uoc chung lon nhat {a} va {b}: {gcd}")
