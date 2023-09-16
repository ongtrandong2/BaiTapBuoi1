order = int(input("nhap so thu tu: "))

def calculate_result(x):
    if x == 1:
        return 2
    else:
        return calculate_result(x-1) + 2*x + 1
    
print("ket qua: ")
print(calculate_result(order))