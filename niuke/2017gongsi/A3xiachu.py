import sys
cai = set([])
lines = sys.stdin.readlines()
for i in lines:
    t = i.split()
    for j in t:
        cai.add(j)
print(len(cai))

