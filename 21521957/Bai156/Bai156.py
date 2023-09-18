
def calculate_factorial_sequence(n):
    sequence = []
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        sequence.append(factorial)
    return sequence

n = int(input("Nhap n: "))

sequence = calculate_factorial_sequence(n)

print("Day gia tri a1, a2, a3, ..., an:")
for i, value in enumerate(sequence):
    print("a" + str(i + 1), "=", value)