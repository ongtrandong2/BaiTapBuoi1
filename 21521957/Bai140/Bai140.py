import math
a = float(input('Nhap a: '))
b = float(input('Nhap b: '))
c = float(input('Nhap c: '))
denta = b * b - 4 * a * c
if(denta <= 0):
    if(denta == 0):
        x = (-b)/(2 * a)
        print("Nghiem la:", x)
    else:
        print("vo nghiem")
else:
    x1 = (-b + math.sqrt(denta))/(2 * a)
    x2=(-b - math.sqrt(denta))/(2 * a)
    print("nghiem x1:", x1, ",x2:", x2)