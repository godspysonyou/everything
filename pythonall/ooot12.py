class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __hash__(self):
        return hash(self.name+self.sex)

    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:return True


p_lst = []
for i in range(84):
    p_lst.append(Person('egon',i,'male'))

#print(p_lst)
print(set(p_lst))
