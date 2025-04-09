class Product:
    def __init__(self, prod_name: str, shop_name: str, price: float):
        self.__prod_name = prod_name
        self.__shop_name = shop_name
        self.__price = price

    def get_name(self):
        return self.__prod_name

    def get_shop_name(self):
        return self.__shop_name

    def get_price(self):
        return self.__price

    def display_info(self):
        print(f"Товар: {self.__prod_name}, Магазин: {self.__shop_name}, Цена: {self.__price} руб.")

class Warehouse:
    def __init__(self, prod_list=None):
        if prod_list is None:
            self.__prod_list = []
        else:
            self.__prod_list = prod_list

    def add_tovar(self, prod):
        if isinstance(prod, Product):
            self.__prod_list.append(prod)
        else:
            raise TypeError("Можно добавлять только объекты класса Tovar")

    def display_by_index(self, index):
        if 0 <= index < len(self.__prod_list):
            self.__prod_list[index].display_info()
        else:
            print('Неверный индекс')

    def display_by_name(self, name):
        found = False
        for product in self.__prod_list:
            if product.get_name().lower() == name.lower():
                product.display_info()
                found = True
        if not found:
            print(f'товар {name} не найден')

    def sort_by_name(self):
        self.__prod_list.sort(key=lambda product: product.get_name())
        self.display_all_tovary()

    def sort_by_shop(self):
        self.__prod_list.sort(key=lambda product: product.get_shop_name())
        self.display_all_tovary()

    def sort_by_cost(self):
        self.__prod_list.sort(key=lambda product: product.get_price(), reverse=True)
        self.display_all_tovary()

    def display_all_tovary(self):
        if not self.__prod_list:
            print("Склад пуст")
        else:
            print("Товары на складе:")
            for product in self.__prod_list:
                product.display_info()

    def __add__(self, other):
        if isinstance(other, Warehouse):
            total_price = sum(t.get_price() for t in self.__prod_list) + \
                          sum(t.get_price() for t in other.__prod_list)
        else:
            total_price = sum(t.get_price() for t in self.__prod_list)

        return total_price

sklad = Warehouse()

sklad.add_tovar(Product("Телевизор", "МегаТех", 65000))
sklad.add_tovar(Product("Монитор", "CompWorld", 28000))
sklad.add_tovar(Product("Клавиатура", "TechMarket", 4000))
sklad.add_tovar(Product("Мышь", "GadgetStore", 2500))
sklad.add_tovar(Product("Принтер", "OfficeTech", 15000))
sklad.add_tovar(Product("Внешний жесткий диск", "DataStore", 12000))
sklad.add_tovar(Product("Игровая консоль", "GameZone", 55000))


# sklad.display_all_tovary()
# sklad.display_by_index(0))
# sklad.display_by_index(3
sklad.sort_by_name()
sklad.sort_by_cost()
# sklad.display_all_tovary()
print(sklad+2)
