import math

def calculate_cos(x):
    cos_x = 1
    term = 1
    n = 1
    
    while abs(term) >= 1e-6:
        term *= -x**2 / ((2*n)*(2*n-1))
        cos_x += term
        n += 1
    
    return cos_x

x = float(input("x (radian): "))

result = calculate_cos(x)
print(f"cos({x}) = {result:.6f}")
