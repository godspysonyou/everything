class Mt:
    c = 5 # 属于类

    def __init__(self):
        self.a = 1 #属于实例
        self.b = 2 #属于实例


if __name__ == "__main__":
    mt1 = Mt()
    mt2 = Mt()
    mt3 = Mt()

    print(mt1.c)
    print(mt2.c)
    mt1.c = 10
    Mt.c = 15
    print(mt1.c)
    print(mt2.c)
    mt2.c = 30
    print(mt2.c)
    Mt.c = 100
    print(mt2.c)
    print(mt3.c)
    Mt.c = 200
    print(mt3.c)