n = int(input("Nhap n: "))
s = 0
i = 1
while i <= n:
    s = pow(i + s, (float(1)/ (i + 1)))
    i = i + 1
print("S(", n, ") = ", s)
