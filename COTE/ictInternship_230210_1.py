import sys
input = sys.stdin.readline

def getGroupedAnagrams(words):
    cnt = 0
    for i in range(0, len(words)):
        for k in range(0, len(words[i])):
            for g in range(i, len(words)):
                if words[i][k] in words[g]:
                    if k == len(words[i]) - 1:
                        cnt += 1
                    continue
                else:
                    break
    return cnt

n = int(input())
li = list()

for _ in range(0, n):
    li.append(input().rstrip())
li = sorted(li, key=len)
lenSameArr = [[] * len(li) for _ in range(0, len(li))]
lenSameArr[0].append(li[0])
tmp = 0

# 길이가 같은 배열끼리 묶기
for i in range(0, len(li) - 1):
    if len(li[i]) == len(li[i + 1]):
        # tmp += 1
        lenSameArr[tmp].append(li[i + 1])
    else:
        tmp += 1
        lenSameArr[tmp].append(li[i + 1])

print(getGroupedAnagrams(lenSameArr))
