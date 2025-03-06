class Math:
    @staticmethod
    def addition( x, y):
        print(x+y)
    @staticmethod
    def subtraction(x, y):
        print(x-y)
    @staticmethod
    def multiplication(x, y):
        print(x*y)
    @staticmethod
    def division(x, y):
        try:
            print(x//y)
        except ZeroDivisionError:
            print('Делить на ноль нельзя')
math = Math()
math.subtraction(100,50)
Math.addition(4,6)
Math.subtraction(4,8)
Math.multiplication(22,3)
Math.division(2,0)
Math.division(4,2)