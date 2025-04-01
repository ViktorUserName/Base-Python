import math
cat_a = 5
cat_b = 10

def area_of_the_triangle(a,b):
    return print(f"Площадь равна {(a*b)/2 if str((a*b)/2)[-1] != '0' else int((a*b)/2)}")


def hypotinuse(a,b):
    return print(f"Гипотинуза: {int(math.sqrt(a**2+b**2))}")

area_of_the_triangle(cat_a, cat_b)
hypotinuse(cat_a,cat_b)
