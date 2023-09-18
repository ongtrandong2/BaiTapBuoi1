def find_tens_place(n):
    tens_digit = (n // 10) % 10
    return tens_digit


n = int(input("Nhap n: "))

tens_digit = find_tens_place(n)
print(f"Chu so hang chuc cua {n} la: {tens_digit}")
