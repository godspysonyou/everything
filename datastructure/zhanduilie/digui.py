'''
递归算法的优点是结构简单，逻辑清晰，并且易于阅读；而其缺点是效率地下，所需要的内存
空间较多，优化十分困难。

至少满足3个条件才适合使用递归
1）待解决问题可以被分解为规模更小但和原问题有相同解法的字问题。
2）子问题的个数必须是有限的，相应的，递归调用的次数也必须是有限的
3）子问题是可解的，即必须存在递归出口
'''


'''
递归转化为非递归思路：
1）若当前正在进行递归函数的调用但还没达到递归出口条件，则将该函数的所有信息（如函数形参、局部变量和返回值）保存到栈空间
2）每一次函数的递归调用均对应栈空间里的一个或多个数据，可通过申明类并实例化来存放这些数据
3）当递归调用返回时，需执行出栈操作以恢复其调用者的相关数据。若有数据需返回，可将其放入调用者对应的栈空间里，从而通过子问题
的求解实现愿问题的求解。
4）栈顶元素对应当前函数的信息，该函数调用者的信息对应次栈顶（即栈顶的直接先驱）元素，所以函数调用顺序与栈中数据的排列顺序相反。
'''

'新注释方式'

from datastructure.zhanduilie.stack import SequenceStack

class Digui:
    count = 0
    def fact(self,n):
        if n == 0:
            return 1
        else:
            return self.fact(n-1)*n

    def fibonacci(self, n):
        if n==1:
            return 1
        elif n==2:
            return 1
        else:
            return self.fibonacci(n-1)+self.fibonacci(n-2)

    def testFibonacci(self):
        num = int(input('请输入需计算第几项斐波那契数：'))
        while num<1:
            num=int(input('请重新输入需计算第几项斐波那契数：'))
        print('第',num,'项斐波那契数为',self.fibonacci(num))

    # 将编号为n的金片从NA针移动到NC针
    def move(self, NA, n, NC):
        self.count += 1
        print('第',self.count,'次移动：将第',n,'号金片从',NA,'移到',NC)

    # 将NA针上的n个金片移到NC针上的函数
    def HanoiTower(self, n, NA, NB, NC):
        if n==1:
            self.move(NA,1,NC)
        else:
            self.HanoiTower(n-1,NA,NC,NB)
            self.move(NA,n,NC)
            self.HanoiTower(n-1,NB,NA,NC)

    def testHT(self):
        n = int(input('请输入第一根针上共有多少个金片：'))
        while n <= 0:
            n = int(input('请重新输入第一根针上有多少个金片：'))
        num1 = input('请输入第一根针的编号为：')
        num2 = input('请输入第二根针的编号为：')
        num3 = input('请输入第三根针的编号为：')
        print('移动过程如下：')
        self.HanoiTower(n, num1, num2, num3)

class FactElements:
    def __init__(self):
        self.labelN = None
        self.N = None
        self.F = None

class FeiDigui:
    # 阶乘非递归算法
    def factorial(self, n):
        fe = FactElements()
        fe.labelN = 2
        fe.N = n
        st = SequenceStack(10)
        st.pushStack(fe)
        while True:
            tFE = st.getTopStack()
            if tFE.N >= 1:
                temp = FactElements()
                temp.labelN = 1
                temp.N = tFE.N - 1
                st.pushStack(temp)
            else:
                tFE.F = 1
                break

        while True:
            tFE = st.getTopStack()
            if tFE.labelN == 1:
                st.popStack()
                temp = st.getTopStack()
                temp.F = tFE.F*temp.N
            tFE = st.getTopStack()
            if tFE.labelN == 2:
                tFE = st.popStack()
                f = tFE.F
                break
        print('求解的结果为：',tFE.N,'!=',f)

class HanoiElements:
    def __init__(self):
        self.Tag = 0
        self.N = None
        self.A = None
        self.B = None
        self.C = None

# 熟练度不够
class TestHanioTower:
    def __init__(self):
        self.count = 0

    def move(self, NA, n, NC):
        self.count = self.count + 1
        print('第',self.count,'次移动：将第',n,'号金片从',NA,'移到',NC)

    def hanioTower(self, n, NA, NB, NC):
        he = HanoiElements()
        he.N = n
        he.A = NA
        he.B = NB
        he.C = NC
        st = SequenceStack(20)
        st.pushStack(he)
        while not st.isEmptyStack():
            while True:
                tHE = st.getTopStack()
                if tHE.N > 1 and tHE.Tag == 0:
                    temp = HanoiElements()
                    temp.N = tHE.N - 1
                    temp.A = tHE.A
                    temp.B = tHE.C
                    temp.C = tHE.B
                    st.pushStack(temp)
                elif tHE.N == 1 and tHE.Tag == 0:
                    self.move(tHE.A, tHE.N, tHE.C)
                    tHE.Tag = 1
                    break
            while not st.isEmptyStack():
                tHE = st.getTopStack()
                if tHE.Tag == 1:
                    st.popStack()
                else:
                    break
            if st.isEmptyStack():
                break
            temp = st.getTopStack()
            self.move(temp.A, temp.N, temp.C)
            temp.Tag = 1
            t = HanoiElements()
            t.N = temp.N-1
            t.B = temp.A
            t.A = temp.B
            t.C = temp.C
            st.pushStack(t)




if __name__ == '__main__':
    # d = Digui()
    # d.testFibonacci()
    # d = Digui()
    # d.testHT()
    # tf = FeiDigui()
    # tfn = int(input('请输入待求阶乘的数：'))
    # tf.factorial(tfn)

    t = TestHanioTower()
    t.hanioTower(3,'A','B','C')