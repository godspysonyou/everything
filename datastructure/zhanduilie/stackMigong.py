from datastructure.zhanduilie.stack import SequenceStack

directions = [(0,1),(1,0),(0,-1),(-1,0)]

class MiGong:

    # 判断当前位置是否可以走
    def isPossiblePass(self, mazeroute, position):
        if mazeroute[position[0]][position[1]] == 0:
            route = True
        else:
            route = False
        return route

    # 将走过的位置设为2
    def passedMark(self, mazeroute, position):
        mazeroute[position[0]][position[1]] = 2

    # 输出迷宫路径的函数
    def printRoute(self, exit1, st):
        print('从出口到入口的路径为：')
        print(exit1, end=' ')
        i = 1
        while not st.isEmptyStack():
            print(st.popStack()[0], end=' ')
            i = i + 1
            if i % 10 == 0:
                print()

    # 变量nxt的取值，当前位置的右方0，当前位置的下方1，左方2，上方3

    # 寻找迷宫路径的函数
    def findMazeRoute(self, mazeroute, enter, exit1):
        st = SequenceStack(100)
        position = enter
        nxt = 0
        while True:
            if position == exit1:
                self.printRoute(exit1, st)
                return
            else:
                self.passedMark(mazeroute, position)

                # for else 用法
                for i in range(nxt, 4):
                    nextPosition = (position[0]+directions[i][0],position[1]+directions[i][1])
                    if self.isPossiblePass(mazeroute, nextPosition):
                        st.pushStack((position, i+1)) # 应该是i还是i+1
                        position = nextPosition
                        nxt = 0
                        break
                else:
                    if st.isEmptyStack():
                        break
                    else:
                        position, nxt = st.popStack()
                # if st.isEmptyStack():
                #     break
                # else:
                #     position, nxt = st.popStack()
        print('没有找到通过迷宫的路径')

if __name__ == '__main__':
    mg = MiGong()
    mazeroute = [[1,1,1,1,1,1,0,1,1,1],
                 [1,0,0,0,0,1,0,1,1,1],
                 [1,0,1,1,0,1,0,0,0,1],
                 [1,0,1,1,0,1,1,1,0,1],
                 [1,0,1,1,0,0,0,0,0,1],
                 [1,0,1,1,0,1,1,1,1,1],
                 [1,0,1,1,0,0,0,0,0,1],
                 [1,0,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,0,0,0,0,0],
                 [1,1,1,1,1,1,1,1,1,1]]
    mg.findMazeRoute(mazeroute, enter=(0,6), exit1=(8,9))