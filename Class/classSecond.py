class Person:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name} ")



class Empolee(Person):

    def __init__(self, name, company):
        super().__init__(name)
        self.__company = company

    def display_info(self):
        super().display_info()
        print(f"Company: {self.__company}")

    def __contains__(self, item):
        if item == "name": return True


    def work(self):
        print(f"work in {self.name}")


tom = Empolee("Tom", "AWC")
tom.display_info()
print("name" in tom)
