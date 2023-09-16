x = float(input('Nhap x: '))
n = int(input('Nhap n: '))
s = 0
t = 1
i = 2
dau = -1
while i <= 2 * n:
    t = t * x * x
    s = s + dau * t
    i = i + 2
dau = -dau
print("S( ", x, ",", n, ") la: ", s)
