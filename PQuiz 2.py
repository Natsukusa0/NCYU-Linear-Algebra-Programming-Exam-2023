a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
s = int(0)
for i in range(max(len(a), len(b))):
    if i*i >= len(a) and i*i >= len(b):
        s = i
        break
oa = [[int(0) for i in range(s)]for j in range(s)]
ob = [[int(0) for i in range(s)]for j in range(s)]
o = [[int(0) for i in range(s)]for j in range(s)]
if len(a) < s*s:
    for i in range(len(a), s*s):
        a.append(int(0))
if len(b) < s*s:
    for i in range(len(b), s*s):
        b.append(int(0))
for i in range(s):
    for j in range(s):
        oa[i][j] = (a[s * i + j])
        ob[i][j] = (b[s * i + j])
ob = list(zip(*ob)) 
for i in range(s):
    for j in range(s):
        for k in range(s):
            o[i][j] += oa[i][k] * ob[k][j]
o = list(zip(*o))
for i in o:
    for j in i:
        print(j, end = ' ')
    print()