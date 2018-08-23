def heapadjust(a, i, size):
    left = 2 * i + 1
    right = 2 * i + 2
    max = i
    while i < size / 2: # 非递归写法
        if left < size and a[left] > a[max]:
            max = left
        if right < size and a[right] > a[max]:
            max = right
        if max != i:
            a[i], a[max] = a[max], a[i]
        else:
            break
        i = max
        left = 2 * i + 1
        right = 2 * i + 2
    return a

def buildheap(a, size):
    for i in range(int(size/2))[::-1]:
        heapadjust(a, i, size)
    return a

def heapsort(a, size):
    a = buildheap(a, size)
    for i in range(0,size)[::-1]:
        a[0], a[i] = a[i], a[0]
        a = heapadjust(a, 0, i)
    return a


class Checker:
    def checkDuplicate(self, a, n):
        a = heapsort(a, n)
        for i in range(n-1):
            if a[i]==a[i+1]:
                return True
        return False

if __name__ == '__main__':
    l = [1, 3, 8, 4,2,6]
    print(heapsort(l, 6))