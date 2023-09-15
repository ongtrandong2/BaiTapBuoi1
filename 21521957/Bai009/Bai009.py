import math
n = float(input('Nhap n: '))
r = float(input('Nhap r: '))
S = float(1 / 2) * n * r * r * math.sin(3.14 * 2/n)
print('Dien tich cua da giac deu', n, 'canh noi tiep trong duong tron ban kinh ', r, ' la: ', S)

