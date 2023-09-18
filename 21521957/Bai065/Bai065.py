def find_min_digit(n):
    min_digit = min(int(digit) for digit in str(n))
    return min_digit


n = int(input("nhap n: "))


min_digit = find_min_digit(n)
print(f"chu so nho nhat cua {n} la: {min_digit}")

