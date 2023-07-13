import sys
input = sys.stdin.readline

n = int(input())
difficulty = []
for i in range(0, n):
    a = int(input())
    difficulty.append(a)
difficulty.sort()

exceptNum = round(n * 0.15 + 0.000000001)

if n == 0:
    result = 0
elif exceptNum == 0:
    result = round(sum(difficulty)/len(difficulty) + 0.000000001)
else:
    tmpSum = sum(difficulty[exceptNum:-exceptNum])
    tmpPeople = (len(difficulty[exceptNum:-exceptNum]))
    result = round(tmpSum/tmpPeople + 0.000000001)
print(result)