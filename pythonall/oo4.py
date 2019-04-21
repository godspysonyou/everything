class Weapon:
    def prick(self, obj):  # 这是该装备的主动技能,扎死对方
        obj.life_value -= 500  # 假设攻击力是500


class Person:  # 定义一个人类
    role = 'person'  # 人的角色属性都是人

    def __init__(self, name):
        self.name = name  # 每一个角色都有自己的昵称;
        self.weapon = Weapon()  # 给角色绑定一个武器;


class Dog:
    role = 'dog'

    def __init__(self, name, breed, attack, life_value):
        self.name = name
        self.breed = breed
        self.attack = attack
        self.life_value = life_value

    def bite(self, people):
        people.life_value -= self.attack

egg = Person('egon')
dog1 = Dog('**','**',10,1000)
egg.weapon.prick(dog1)
print(dog1.life_value)
# egg组合了一个武器的对象，可以直接egg.weapon来使用组合类中的所有方法