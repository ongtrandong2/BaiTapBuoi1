def count_digits(n):
    return len(str(n))


n = int(input("nhap n: "))


num_digits = count_digits(n)
print(f"so chu so cua {n} la: {num_digits}")

