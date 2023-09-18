n=int(input("Nhap n: ")) 
tong=0 
t=n 
while(t!=0): 
    dv=t%10 
    tong=tong+dv 
    t=int(t/10) 
print("Tong cac chu so nguyen duong cua n:  ", tong)
