import sys
input = sys.stdin.readline

t = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(0, t):
    m, n, k = map(int, input().split())

    cabbage = [[0] * n for _ in range(0, m)]

    for i in range(0, k):
        a, b = map(int, input().split())
        cabbage[a][b] = 1

