class Person:
    def __init__(self, name='non1', surname='non2',age=0):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def age(self):
        print(self.__age)
        return self.__age
    
    @age.setter
    def age(self, age):
        if 0 < age < 110:
            self.__age = age
        else:
            print('Bad age input')

    
    @property
    def get_name(self):
        return self.__name
    
    def sayHi(self):
        print(f'hi {self.__name} age {self.__age}')
    
person1 = Person("Viktor", "Chiz", 127)
person1.sayHi()
person1.age = 11
person1.sayHi()
print(person1.age)

# person1.setAge(99)
# person1.get_age()
# ---
# first = Person('Viktor')
# print(first._Person__name)
    
# print(person1.name)
# person2 = Person()
# print(person2.name)
# person1.sayHi()


