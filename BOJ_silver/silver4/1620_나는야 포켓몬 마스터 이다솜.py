import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = dict()
question = [0] * m
answer = ""

for i in range(1, n + 1):
    pocketmon = input().rstrip()
    li[pocketmon] = i
    li[i] = pocketmon

for k in range(0, m):
    question = input().rstrip()
    if question.isdigit() == True:
        answer += str(li[int(question)])
        answer += "\n"
    else:
        answer += str(li[question])
        answer += "\n"
    # answer += li[question[k]]

# for k in range(0, m):
#     # 문제가 string을 주어져 인덱스 찾아야할 때
#     # if (str(question) == "<class 'str'>"):
#     try : 
#         answer += str(li.index(str(question[k])))
#         answer += "\n"
#     except:
#         answer += str(li[int(question[k])])
#         answer += "\n"
            
    # elif (str(question.__class__) == "<class 'int'>"):

print(answer.rstrip())