N = int(input())
G = N // 493
rest = N % 493
S = rest // 29
K = rest % 29
if G != 0:
    print(G, 'галлеонов')
if S != 0:
    print(S, 'сиклей')
if K != 0:
    print(K, 'кнатов')
