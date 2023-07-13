import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
li = [] * n
for i in range(0, n):
    clothes, kind = list(input().split())
print()