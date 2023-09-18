def is_valid_triangle(x1, y1, x2, y2, x3, y3):
    if (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) != 0:
        return True
    return False

x1, y1 = map(float, input("(x1, y1): ").split())
x2, y2 = map(float, input("(x2, y2): ").split())
x3, y3 = map(float, input("(x3, y3): ").split())

if is_valid_triangle(x1, y1, x2, y2, x3, y3):
    print("hop le.")
else:
    print("khong hop le.")

