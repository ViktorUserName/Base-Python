# . ПчёлоСлон
# Экземпляр класса инициализируется двумя целыми числами,
# первое относится к пчеле, второе – к слону. Класс реализует
# следующие методы:
# ● fly() – возвращает True, если часть пчелы не меньше части
# слона, иначе – False
# ● trumpet() – если часть слона не меньше части пчелы,
# возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
# ● eat(meal, value) – может принимать в meal только ”nectar”
# или “grass”. Если съедает нектар, то value вычитается из
# части слона, пчеле добавляется. Иначе – наоборот. Не

class ElephBee:
    def __init__(self, elephant:int, bee:int):
        self.elephant = elephant
        self.bee = bee


    def elephant(self):
        return self.elephant

    def fly(self):
        if self.elephant <= self.bee:
            print('True')
            return True
        else:
            print('False')
            return False
    def trumpet(self):
        if self.elephant >= self.bee:
            print('tu-tu-doo-doo')
        else:
            print('wzzzz')

    def eat(self, value, meal):
        if meal not in ('Нектар', 'Трава'):
            print('Можно есть только Нектар или Траву')

        if meal == 'Нектар':
            self.elephant = max(0, self.elephant-value)
            self.bee = min(100, self.bee + value)
        else:
            self.bee = max(0, self.elephant - value)
            self.elephant = min(100, self.bee + value)

first = ElephBee(30, 40)
first.fly()
first.trumpet()
first.eat(30,'Трава')
first.fly()
first.trumpet()
first.eat(300,'Трава')