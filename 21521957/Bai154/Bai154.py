n = int(input('Nhap n: '))
ahh = n
print(ahh)
while ahh != 1:
    if (ahh%2==0):
        ahh = ahh/2
    else:
        ahh = 3*ahh+1
    print(ahh)
