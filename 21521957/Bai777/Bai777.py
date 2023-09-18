import math

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume


radius = float(input("nhap ban kinh: "))


volume = calculate_sphere_volume(radius)
print(f"the tich khoi cau la: {volume:.2f} ")

