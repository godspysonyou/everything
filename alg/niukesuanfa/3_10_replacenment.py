class Replacement:
    def replaceSpace(self, initString, length):
        kongge = 0
        for e in initString:
            if e==' ':
                kongge+=1
        houzui = kongge*2
        newlength = length+houzui
        strs = list(initString)
        strs+=[' ' for i in range(houzui)]
        newlength-=1
        for i in range(0,length)[::-1]:
            if strs[i]!=' ':
                strs[newlength] = strs[i]
                newlength-=1
            else:
                strs[newlength-2:newlength+1] = ['%','2','0']
                newlength-=3
        return ''.join(strs)
if __name__ == '__main__':
    r = Replacement()
    # print(r.replaceSpace('Hello  World', 12))
    print(r.replaceSpace('Mr John Smith',13))
    # s = ['a','b','c']
    # s[1:] = ['d','e']
    # print(s)
