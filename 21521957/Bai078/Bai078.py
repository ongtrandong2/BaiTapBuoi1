
x = float(input("Nhap x x: "))
n = int(input("Nhap n: "))
if n <= 0:
    print(" nphai la so nguyen duong")
elif x == 0 and n == 0:
    print("Tong cua day la 0")
else:
    tong = 0
    for i in range(n + 1):
        tong += x ** i
    print("Tong cua day la:", tong)