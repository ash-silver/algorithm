import sys
input = sys.stdin.readline

n, k = map(int, input().split())
pail = [0] * 1000001
minIndex = 1000001
maxIndex = 0
answer = 0

for _ in range(0, n):
    g, x = map(int, input().split())
    minIndex = min(x, minIndex)
    maxIndex = max(x, maxIndex)
    pail[x] = g
    
step = 2 * k + 1
slice = sum(pail[:step])
answer = slice
for i in range(step, maxIndex + 1):
    slice += pail[i] - pail[i - step]
    answer = max(slice, answer)
print(answer)