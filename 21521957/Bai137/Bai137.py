def f(x):
    if x >= 5:
        return 2*x**2 + 5*x + 9
    else:
        return -2*x**2 + 4*x - 9


x = float(input("x: "))


result = f(x)
print(f"f({x}) = {result}")
