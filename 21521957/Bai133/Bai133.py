x=float(input("Nhap x:   "))
y=float(input("Nhap y:   "))
z=float(input("Nhap z:   "))

if ((x+y>z)and(y+z>x)and(z+x>y)):
    if ((x==y)and(y==z)):
        print("\nTam giac deu.")
    else:
        if((x*x==y*y+z*z)or(y*y==x*x+z*z)or(z*z==x*x+y*y)):
            if((x==y)or(y==z)or(x==z)):
                print("\nTam giac vuong can.")
            else:
                print("\nTam giac vuong.")
        else:
            if((x==y)or(y==z)or(x==z)):
                print("\nTam giac can.")
            else:
                print("\nTam giac thuong.")
else:
    print("\nKhong la tam giac.")
print("\n")
