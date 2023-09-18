n = int(input("Nhap n: "))
s = 1
i = 1
while (i <= n):
    s = s * (1 + float(1 / (i * i)))
    i = i + 1
print("S(", n, ") = ", s)

