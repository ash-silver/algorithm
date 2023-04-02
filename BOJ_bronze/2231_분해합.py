import sys
input = sys.stdin.readline

n = input().rstrip()
result = 0

for i in range(0, int(n)):
    tmp = str(i)
    tmpResult = i
    for k in tmp:
        tmpResult += int(k)
    if tmpResult == int(n):
        result = int(i)
        break
    else:
        continue

        
print(result)

