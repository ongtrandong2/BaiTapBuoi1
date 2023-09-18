import math
n = int(input('Nhap n: '))
s = 0
e = 0.5
i = 1
while e >= math.pow(10,-6):
    e = 1/(i * (i + 1))
    s = s + e 
    i = i + 1
print("S(", n, ") la: ", s)
