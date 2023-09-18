def check_digits_decreasing(n):
    digits = str(n)
    for i in range(len(digits) - 1):
        if digits[i] <= digits[i+1]:
            return False
    return True

n = int(input("nhap n: "))

if check_digits_decreasing(n):
    print("sap xep tu trai sang phai")
else:
    print("khong duoc sap tu trai sang phai")