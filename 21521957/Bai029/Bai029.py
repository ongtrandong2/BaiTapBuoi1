def calculate_series_sum(n):
    total = 0
    for i in range(1, n+1):
        total += 1/i
    return total


n = int(input("Nhap n: "))


result = calculate_series_sum(n)
print(f"tong day tu 1/1 den 1/{n} la: {result:.2f}")
