class Person:
    role = 'person'
    def __init__(self, name, attack, life_value):
        self.name = name
        self.attack = attack
        self.life_value = life_value
    def walk(self):
        print('person is walking...')

# print(Person.role)
# print(Person.walk)
#
# egg = Person('egon', 10, 1000)

# print(egg.name)
# print(egg.walk())
#
# print('_____')
# print(Person.__name__)
# print(Person.__doc__)
# print(Person.__base__)
# print(Person.__bases__)
# print(Person.__dict__)
# print(Person.__module__)
# print(Person.__class__)
# print()
#
# print(egg.name)
# print(egg.attack)
# print(egg.life_value)