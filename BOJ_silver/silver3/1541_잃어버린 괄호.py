import sys
input = sys.stdin.readline

sentence = input().rstrip()
answer = 0
plusSen = sentence.split("-")

for i in range(0, len(plusSen)):
    tmpSum = 0        
    tmpLi = plusSen[i].split("+")
    for k in tmpLi:
        tmpSum += int(k)
    if i == 0:
        answer = tmpSum
    else:
        answer -= tmpSum
    
    

print(answer)