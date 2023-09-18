
n = int(input("Nhap n: "))
if n <= 0:
    print("n khong dat yeu cau")
else:
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            tong += i
    print("Ket qua: ", tong)