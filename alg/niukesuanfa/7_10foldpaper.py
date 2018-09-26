class FoldPaper:
    # def __init__(self):
    #     self.ret = []
    def foldPaper(self, n):
        ret = []
        self.fold(1, n, True, ret)
        return ret
        pass

    def fold(self, i, N, down, ret):
        if (i > N):
            return
        self.fold(i + 1, N, True, ret)
        if down:
            ret.append('down')
        else:
            ret.append('up')
        self.fold(i + 1, N, False, ret)

if __name__ == '__main__':
    f = FoldPaper()
    print(f.foldPaper(2))
