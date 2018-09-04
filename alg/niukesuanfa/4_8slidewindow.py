class SlideWindow:
    def slide(self, arr, n, w):
        if not arr or w<1 or n<w:
            return None
        qmax = []
        res = [0 for i in range(n-w+1)]
        index = 0
        for i in range(n):
            while (qmax and arr[qmax[-1]]<=arr[i]): # 右出
                qmax.pop(-1)
            qmax.append(i)
            if (qmax[0] == i-w): # 队列头的有效期（在不右出的情况下）
                qmax.pop(0)
            if (i>=w-1): # 在第三格开始就要放数字
                res[index] = arr[qmax[0]]
                index+=1
        return res

if __name__ == '__main__':
    s = SlideWindow()
    print(s.slide([4,3,5,4,3,3,6,7],8,3))