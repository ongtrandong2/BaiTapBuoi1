def calculate_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i*(i+1)*(i+2)
    return total


n = int(input("Nhap n: "))


result = calculate_sum(n)
print(f"tong tu 1*2*3 den {n}*({n}+1)*({n}+2) la: {result}")
