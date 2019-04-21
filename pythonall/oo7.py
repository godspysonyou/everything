class Person:
    role = 'person'

    def __init__(self, name, attack, life_value, money):
        self.name = name
        self.attack = attack
        self.life_value = life_value
        self.money = money

    def attackone(self, dog):
        dog.life_value -= self.attack


class Dog:
    role = 'dog'

    def __init__(self, name, breed, attack, life_value):
        self.name = name
        self.breed = breed
        self.attack = attack
        self.life_value = life_value

    def bite(self, people):
        people.life_value -= self.attack


class Weapon:
    def __init__(self, name, price, attack, life_value):
        self.name = name
        self.price = price
        self.attack = attack
        self.life_value = life_value

    def update(self, obj):
        obj.money -= self.price
        obj.attack += self.attack
        obj.life_value += self.life_value

    def prick(self, obj):
        obj.life_value -= 500


lance = Weapon('长矛', 200, 6, 100)
egg = Person('egon', 10, 1000, 600)
ha2 = Dog('二愣子', '哈士奇', 10, 1000)

if egg.money > lance.price:
    lance.update(egg)
    egg.weapon = lance

print(egg.money, egg.life_value, egg.attack)

print(ha2.life_value)

egg.attackone(ha2)
print(ha2.life_value)
egg.weapon.prick(ha2)
print(ha2.life_value)