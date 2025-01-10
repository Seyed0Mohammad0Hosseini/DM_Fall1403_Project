from collections import deque, defaultdict
import math

# Constants
maxm = 4 * 10 ** 5 + 2
mod = 10**9 + 7

# Variables
l, r, mid = 0, 0, 0
n, m = 0, 0
dis = [0] * maxm
sum_arr = [0] * maxm
darage = [0] * maxm
ss, mm = 0, 0
q = deque()
g = defaultdict(list)
z = defaultdict(list)
sath = [0] * maxm
gos = [False] * maxm
pedaret = list(range(maxm))
pars1 = [0] * maxm
pars2 = [0] * maxm
st = set()
rp = [0] * maxm
w = [(0, 0)] * maxm
ri = [(0, 0)] * maxm
seg = [0] * (maxm * 4)
vis = [False] * maxm
mp = {}
res1 = [0] * maxm
res2 = [0] * maxm
par = [0] * maxm
tek = [0] * 3002
voj = [[False] * ((1 << 14) + 7) for _ in range(150)]

def cmp(x):
    r = 0
    for i in range(14):
        if (1 << i) & x:
            r += 1
    qw = 1
    for i in range(26, 26 - r, -1):
        qw *= i
        qw %= mod
    return qw

def main():
    global n, s, l, mid
    s = input()
    n = len(s)
    a = ["1", "0", "11", "10", "01", "00", "111", "110", "101", "100", "011", "010", "001", "000"]
    g[0].extend([2, 3, 6, 7, 8, 9])
    g[1].extend([4, 5, 10, 11, 12, 13])
    g[2].extend([6, 7])
    g[3].extend([8, 9])
    g[4].extend([10, 11])
    g[5].extend([12, 13])
    voj[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(14):
            if len(a[j]) > i:
                break
            t = s[i - len(a[j]):i]
            if t == a[j]:
                for u in range(1 << 14):
                    if voj[i - len(a[j])][u]:
                        voj[i][u | (1 << j)] = True
                        
    for i in range(1, 1 << 14):
        if not voj[n][i]:
            continue
        t = ""
        vec = []
        for j in range(14):
            if (1 << j) & i:
                vec.append(j)
                t += a[j]
        ok = False
        for k in vec:
            for j in vec:
                for y in g[k]:
                    if y == j:
                        ok = True
        if ok:
            continue
        if voj[n][i]:
            l += 1
            mid += cmp(i)
            mid %= mod
            
    print(l)
    print(mid)
    
if __name__ == "__main__":
    main()
