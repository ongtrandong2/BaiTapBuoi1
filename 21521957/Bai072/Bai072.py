
n = int(input("Nhap n: "))
if n <= 0:
    print("n phai la so nguyen duong")
else:
    tong = 0
    sum_so_far = 0
    for i in range(1, n + 1):
        sum_so_far += i
        tong += 1 / sum_so_far
    print("Ket qua: ", tong)