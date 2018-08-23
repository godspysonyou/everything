class Transform:
    def chkTransform(self, A, lena, B, lenb):
        t1 = list(A)
        t2 = list(B)
        t1 = list(map(ord, t1))
        t2 = list(map(ord, t2))
        if (not A or not B or (lena != lenb)):
            return False
        maps = [0 for i in range(256)]
        for i in range(lena):
            maps[t1[i]] += 1
        for j in range(lenb):
            maps[t2[j]] -= 1
            if maps[t2[j]] < 0:
                return False

        return True

if __name__ == '__main__':
    maps = [0 for i in range(25)]
    t = Transform()
    print(t.chkTransform('abc', 3, 'bca', 3))
    # a = 'aab'
    # list(a)
    # print(list(a))

