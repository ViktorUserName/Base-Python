import math
class Sphere:
    def __init__(self, r = 1, x = 0, y = 0, z = 0):
        self.r = r
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        v = (4/3) * math.pi * self.r**3
        print(f'Объем {v:.2f}')
    def get_square(self):
        s =  4 * math.pi * self.r**2
        print(f'Площадь {s:.2f}')
    def get_radius(self):
        print(f'радиус {self.r}')
    def get_center(self):
        print(f'центр находится {(self.x, self.y, self.z)}')
    def set_radius(self,r):
        self.r = r

new_sw = Sphere(3,2,3,4)

new_sw.get_volume()
new_sw.get_square()
new_sw.get_center()
new_sw.get_radius()

new_sw.set_radius(10)
new_sw.get_radius()