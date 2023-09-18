
n = int(input("Nhap n: "))
if n <= 0:
    print("n khong dat yeu cau")
else:
    has_even_digit = False
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            has_even_digit = True
            break
        n //= 10
    if has_even_digit:
        print("co chu so chan")
    else:
        print("Khong co chu so chan")
