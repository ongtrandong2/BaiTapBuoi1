n = int(input('Nhap n: '))
flag =1
t=n
while(t>1):
    du = t%3
    if du !=0 :
        flag =0
    t=t/3
if flag ==1:
    print(n,'co dang 3^m')
else:
    print(n,'khong co dang 3^m')
        


