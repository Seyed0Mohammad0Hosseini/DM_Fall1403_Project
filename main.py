from collections import defaultdict


# Constants
mod = 10 ** 9 + 7

# Variables
shoomarande, r, vazn = 0, 0, 0
n = 0
graph = defaultdict(list)
vojood = [[False] * ((1 << 14) + 7) for _ in range(150)]


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
    global n, stiring, shoomarande, vazn
    stiring = input()
    n = len(stiring)
    a = ["1", "0", "11", "10", "01", "00", "111", "110", "101", "100", "011", "010", "001", "000"]
    graph[0].extend([2, 3, 6, 7, 8, 9])
    graph[1].extend([4, 5, 10, 11, 12, 13])
    graph[2].extend([6, 7])
    graph[3].extend([8, 9])
    graph[4].extend([10, 11])
    graph[5].extend([12, 13])
    vojood[0][0] = True



    for i in range(1, n + 1):
        for j in range(14):
            if len(a[j]) > i:
                break
            t = stiring[i - len(a[j]):i]
            if t == a[j]:
                for u in range(1 << 14):
                    if vojood[i - len(a[j])][u]:
                        vojood[i][u | (1 << j)] = True

    for i in range(1, 1 << 14):
        if not vojood[n][i]:
            continue
        t = ""
        vec = []
        for j in range(14):
            if (1 << j) & i:
                vec.append(j)
                t += a[j]
        ok = False
        # for k in vec:
        #     for j in vec:
        #         for y in graph[k]:
        #             if y == j:
        #                 ok = True
        for k in vec:
             for j in vec:
                 for y in graph[j]:
                     if y == k:
                         ok = True
        if ok:
            continue
        if vojood[n][i]:
            shoomarande += 1
            vazn += cmp(i)
            vazn %= mod

    print(shoomarande)
    print(vazn)


if __name__ == "__main__":
    main()




