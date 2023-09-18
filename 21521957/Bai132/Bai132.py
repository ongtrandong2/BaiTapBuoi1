
def check_point_in_triangle(xA, yA, xB, yB, xC, yC, xM, yM):
    triangle_area = abs((xA*(yB-yC) + xB*(yC-yA) + xC*(yA-yB)) / 2)
    sub_triangle_1_area = abs((xM*(yA-yB) + xA*(yB-yM) + xB*(yM-yA)) / 2)
    sub_triangle_2_area = abs((xM*(yB-yC) + xB*(yC-yM) + xC*(yM-yB)) / 2)
    sub_triangle_3_area = abs((xM*(yC-yA) + xC*(yA-yM) + xA*(yM-yC)) / 2)

    if triangle_area == sub_triangle_1_area + sub_triangle_2_area + sub_triangle_3_area:
        return True
    else:
        return False

xA, yA = map(float, input("Nhap toa do diem A (xA, yA): ").split())
xB, yB = map(float, input("Nhap toa do diem B (xB, yB): ").split())
xC, yC = map(float, input("Nhap toa do diem C (xC, yC): ").split())
xM, yM = map(float, input("Nhap toa do diem M (xM, yM): ").split())

if check_point_in_triangle(xA, yA, xB, yB, xC, yC, xM, yM):
    print("M nam trong tam giac.")
else:
    print("M khong nam trong tam giac")