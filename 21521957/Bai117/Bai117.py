n = int(input("Nhap n: "))
att = - 1
at = 3
t = 2
i = 2
while i <= n:
    t = t * 2
    ahh = 5 * t + 5 * at - att
    i = i + 1
    att = at
    at = ahh
print("So hang thu ", n, "cua day la ", ahh)

