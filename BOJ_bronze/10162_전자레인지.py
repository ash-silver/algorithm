import sys
input = sys.stdin.readline

microwave = [300, 60, 10]

t = int(input())

if t % 10 == 0:
    answer = list()
    for i in microwave:
        tmp = (t // i)
        t -= i * tmp
        answer.append(tmp)
    for i in answer:
        print(i, end=" ")
else:
    print(-1)        