import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)
i = 0
answer = 0
max = 0

while i < m:

    for g  in range(0, k):
        answer += li[0]
        i += 1
        if i >= m:
            break
    if i < m:
        answer += li[1]
        i += 1

print(answer)    

