import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    side1 = calculate_distance(x1, y1, x2, y2)
    side2 = calculate_distance(x2, y2, x3, y3)
    side3 = calculate_distance(x3, y3, x1, y1)

    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area


x1, y1 = map(float, input("nhap A (x y): ").split())
x2, y2 = map(float, input("Nhap b B (x y): ").split())
x3, y3 = map(float, input("Nhap C (x y): ").split())

area = calculate_triangle_area(x1, y1, x2, y2, x3, y3)
print(f"dien tich: {area:.2f}")

