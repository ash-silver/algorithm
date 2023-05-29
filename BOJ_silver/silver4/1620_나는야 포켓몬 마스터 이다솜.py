import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = dict()
answer = ""

for i in range(1, n + 1):
    pocketmon = input().rstrip()
    li[pocketmon] = i
    li[i] = pocketmon

for k in range(0, m):
    question = input().rstrip()
    if question.isdigit() == True:
        print(str(li[int(question)]))
        # answer += "\n"
    else:
        print(str(li[question]))
        # answer += "\n"

print(answer.rstrip())