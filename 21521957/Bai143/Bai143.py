def is_perfect_number(n):
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_of_divisors == n


n = int(input("n: "))


if is_perfect_number(n):
    print(f"{n} hop le")
else:
    print(f"{n} khong hop le.")
