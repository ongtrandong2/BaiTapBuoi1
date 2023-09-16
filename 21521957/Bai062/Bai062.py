n = int(input('Nhap n: '))
s = 0
t = n
while t!=0:
    dv = t % 10
    if (dv % 2 == 0):
        s = s + dv
    t = t // 10
print("Tổng các chữ số chẵn của số nguyên dương ", n, "la: ", s)