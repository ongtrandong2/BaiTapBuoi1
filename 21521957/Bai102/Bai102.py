
def calculate_sequence(n):
    if n < 1:
        return None

    total = 0.0
    for i in range(1, n+1):
        denominator = 2 * i
        term = 1 / denominator
        total += term

    return total

n = int(input("Nhap n: "))

result = calculate_sequence(n)
if result is None:
    print("n khong dat yeu cau")
else:
    print("ket qua: %.6f" % result)