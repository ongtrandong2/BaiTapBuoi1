
n = int(input("Nhap n: "))
if n <= 0:
    print("n khong dat yeu cau.")
else:
    tich = 1
    while n > 0:
        digit = n % 10
        tich *= digit
        n //= 10
    print("Ket qua", tich)