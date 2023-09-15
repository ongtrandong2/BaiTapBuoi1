import math
n = int(input('Nhap n: '))
s = 0 
e = 4
dau = 1
i = 1
while e >= math.pow(10,-6):
    e = 4/i
    s = s + dau * e
    i = i + 2
    dau = -dau
print("Leibniz pi:", s)
