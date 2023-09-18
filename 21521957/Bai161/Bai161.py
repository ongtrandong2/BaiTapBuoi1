def is_digits_increasing(n):
    str_n = str(n)
    for i in range(len(str_n)-1):
        if str_n[i] > str_n[i+1]:
            return False
    return True

n = int(input("n: "))


if is_digits_increasing(n):
    print("hop le")
else:
    print("khong hop le")
