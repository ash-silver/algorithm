import sys
input = sys.stdin.readline

t = int(input())
answer = []
for i in range(0, t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((abs(x2 - x1))**2 + abs((y2 - y1))**2)**(1/2)

    if distance == 0:
        if r1 == r2:
            answer.append(-1)
        else:
            answer.append(0)
    elif abs(r2 - r1) <distance < (r1 + r2):
        answer.append(2)
    elif distance == (r1 + r2) or distance == abs(r2 - r1):
        answer.append(1)    
    else :
        answer.append(0)

for i in answer:
    print(i)