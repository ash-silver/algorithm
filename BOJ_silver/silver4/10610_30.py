import sys
input = sys.stdin.readline

n = list(map(int, input().rstrip()))
answer = ""
if 0 not in n:
    answer = "-1"
elif sum(n) % 3 != 0:
    answer = "-1"
else:
    n.sort(reverse=True)
    for i in n:
        answer += str(i)

print(answer)
