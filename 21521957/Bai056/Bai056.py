n = int(input('Nhap n: '))
dem = 0
i = 2
while i <= n:
    if (n % i == 0):
        dem = dem + 1
    i = i + 2
print("so luong uoc so chan cua so nguyen duong ", n, "la: ", dem)
