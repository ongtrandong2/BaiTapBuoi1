a = float(input('Nhap a: '))
b = float(input('Nhap b: '))
if(a > b):
    temp = a
    a = b 
    b = temp
print("thu tu tang dan : ", a, ",", b)