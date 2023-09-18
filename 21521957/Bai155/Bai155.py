
def generate_sequence(n):
    sequence = [2**(i+1) for i in range(1,n+1)]
    return sequence


n = int(input("n: "))

sequence = generate_sequence(n)
print(f"ket qua: {sequence}")