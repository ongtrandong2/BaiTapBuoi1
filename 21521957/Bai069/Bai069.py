x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
s = 0
t = 1
i = 1
while i <= n:
    t = t * x
    s = s + t
    i = i + 1
print("S(", x, ",", n, ") = ", s)


