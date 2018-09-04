class TwoStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.outlist = []
    def twoStack(self, ope, n):
        for i in ope:
            if i==0:
                if self.stack2:
                    t = self.stack2.pop(-1)
                    self.outlist.append(t)
                else:
                    while self.stack1:
                        t = self.stack1.pop(-1)
                        self.stack2.append(t)
                    if self.stack2:
                        t = self.stack2.pop(-1)
                        self.outlist.append(t)
            else:
                self.stack1.append(i)
        return self.outlist


if __name__ == '__main__':
    t = TwoStack()
    print(t.twoStack([1,2,3,0,4,0],6))
