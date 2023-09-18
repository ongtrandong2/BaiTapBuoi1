
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    gcd = find_gcd(a, b)
    lcm = (a * b) // gcd
    return lcm

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

lcm = find_lcm(a, b)

print("Ket qua: ",  lcm)