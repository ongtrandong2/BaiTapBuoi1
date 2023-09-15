n = int(input('Nhap n: '))
lc = n % 10
dem = 0
t = n
while t != 0:
    dv = t % 10
    if(dv > lc):
        lc = dv
    t = t // 10
t = n
while(t != 0):
    dv = t % 10
    if(dv == lc):
        dem = dem + 1
    t = t // 10
print("so luong chu so lon nhat cua", n,"la: ", dem)
