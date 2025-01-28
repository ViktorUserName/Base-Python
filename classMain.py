class Person:
    def __init__(self, name='non1', surname='non2', age='18'):
        self.name = name
        self.surname = surname
        self.age = age
    def sayHi(self):
        print(f'hi {self.name}')
    
person1 = Person("Viktor", "Chiz", 27)
print(person1.name)
person2 = Person()
print(person2.name)
person1.sayHi()
