

n = int(input("Nhap n: "))
if n < 1:
    print("n khong phai la so nguyen duong")
else:
    tong = 0
    for i in range(1, n + 1):
        tong += 1 / (i * (i + 1))
    print("Tong la:", tong)