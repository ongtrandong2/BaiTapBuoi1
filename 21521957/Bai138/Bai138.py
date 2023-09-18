def calculate_f(x):
    if x < 0:
        return -2*x**3 + 6*x + 9
    elif 0 <= x <= 1:
        return 5*x - 7
    else:
        return 2*x**3 + 5*x**2 - 8*x + 3


x = float(input("nhap x: "))


result = calculate_f(x)

print("Ket qua:", result)