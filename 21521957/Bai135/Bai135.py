x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
n = x
while n <= y:
    dk1 = ((n % 4 == 0) & (n % 100 != 0))
    dk2= (n % 400 == 0)
    if dk1 or dk2:
        print("Nam", n, "la nam nhuan \n")
    n = n + 1

