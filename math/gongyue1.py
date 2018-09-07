# 更相减损
def gengxiang(a,b):
    if a==b:
        return a
    # while a%2==0 and b%2==0:
    #     a = int(a/2)
    #     b = int(b/2)

    while a!=b:
        if a>b:
            maxo = a
            mino = b
        else:
            maxo = b
            mino = a
        a = maxo-mino
        b = mino
    return a

def maxc(a, b):
    if a>b:
        return a
    return b


# 欧几里得，辗转相除
def zhanzhuan(a, b):
    if a==b:
        return a
    if a>b:
        maxo = a
        mino = b
    else:
        maxo = b
        mino = a
    shang = int(maxo/mino)
    yu = maxo%mino
    if yu==0:
        return mino
    else:
        return zhanzhuan(mino,yu)

if __name__ == '__main__':
    print(zhanzhuan(70,80))