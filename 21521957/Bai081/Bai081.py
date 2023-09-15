x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
s = 0
m = 1
i = 0
while i <= n:
    m = m * (x + i)
    s = s + float(1)/m
    i = i + 1
print("S(", x, ",", n, ") = ", s)


