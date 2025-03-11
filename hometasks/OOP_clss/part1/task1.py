class Soda:
    def __init__(self, flavor='обычная'):
        self.__flavor = flavor

    def get_flavor(self):
        print(f'У вас {self.__flavor}  газировкa')


cola = Soda()
cola.get_flavor()

cherry_cola = Soda('вишневая')
cherry_cola.get_flavor()