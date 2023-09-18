x = float(input('Nhap x: '))
n = int(input('Nhap n: '))
s = 1
t = 1
i = 1
while i <= n:
    t = t * x
    s = s + (i + 1) * t
    i = i + 1
print("S( ", x, ",", n, ") la: ", s)