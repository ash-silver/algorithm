import re
import sys
input = sys.stdin.readline

str = input().rstrip()

str = re.sub("\[", "", str)
str = re.sub("\]", "", str)
arr = list()
arr = str.split(', ')
answer = [0, 0]
result = 0

for i in range(0, len(arr), 3):
    win = int(arr[i])
    purchase = int(arr[i + 1]) + 1
    probability = float(win/purchase)

    if probability > answer[0]:
            answer[0] = probability
            answer[1] = int(arr[i + 2])    
            result = (i + 3) // 3
    elif probability == answer[0]:
        if int(arr[i + 2]) > answer[1]:
            result = (i + 3) // 3


print(result)
