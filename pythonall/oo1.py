def person(name, age, sex, job):
    def walk(person):
        print("person %s is walking..." % person['name'])
    data = {
        'name':name,
        'age':age,
        'sex':sex,
        'job':job,
        'walk':walk
    }
    return data

def dog(name, dog_type):
    def bark(dog):
        print("dog %s:wang.wang..wang..." % dog['name'])
    data = {
        'name':name,
        'type':dog_type,
        'bark':bark
    }
    return data

d1 = dog("haha","京吧")
p1 = person("闫帅",36,"F","运维")
p2 = person("egon",27,"F","Teacher")





d1['bark'](p1)

