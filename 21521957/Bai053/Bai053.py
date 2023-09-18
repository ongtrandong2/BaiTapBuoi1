def find_odd_divisors(n):
    odd_divisors = []
    for i in range(1, n + 1, 2):
        if n % i == 0:
            odd_divisors.append(i)
    return odd_divisors


n = int(input("nhap n: "))


odd_divisors = find_odd_divisors(n)
print(f"uoc le cua {n} la: {odd_divisors}")

