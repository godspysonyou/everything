from pythonall.oo2 import Person


class Dog:
    role = 'dog'

    def __init__(self, name, breed, attack, life_value):
        self.name = name
        self.breed = breed
        self.attack = attack
        self.life_value = life_value

    def bite(self, people):
        people.life_value -= self.attack


ha2 = Dog('二流子', '哈士奇', 10, 1000)
egg = Person('egon', 10, 1000)
print(egg.life_value)
ha2.bite(egg)
print(egg.life_value)