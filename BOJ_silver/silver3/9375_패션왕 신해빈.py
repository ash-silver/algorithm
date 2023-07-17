import sys
input = sys.stdin.readline

t = int(input())
answer = []

for k in range(0, t):
    n = int(input())

    clothes = dict()
    for i in range(0, n):
        name, kind = input().split()
        if kind in clothes:
            clothes[kind].append(name)
        else:
            clothes[kind] = [name]
    tmp = 1
    for i in clothes.keys():
        tmp *= (len(clothes[i]) + 1)
    answer.append(tmp - 1)

for i in answer:
    print(i)