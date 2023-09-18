
n = int(input("Nhập số nguyên dương n: "))


if n == 0:
    print("Giá trị của n phải là số nguyên dương khác 0.")
else:

    tong = 0


    for i in range(1, n + 1):
        tong += 1 / (2 * i)


    print("Tổng của dãy là:", tong)