def calculate_sequence_term(a, n):
    if n < 1:
        return None

    if n == 1:
        return a

    term = a
    for i in range(2, n + 1):
        term = 5 * term + 2.3 * i - 6.7 * i + 12

    return term

a = int(input("Nhap a: "))
n = int(input("Nhap n: "))

result = calculate_sequence_term(a, n)
if result is None:
    print("a khong hop le")
else:
    print("so thu ", n, "cua day:", result)
