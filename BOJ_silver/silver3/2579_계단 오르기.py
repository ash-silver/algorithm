import sys
input = sys.stdin.readline

# n = int(input())
# stair = [int(input()) for _ in range(0, n)]
# dp = [0] * n
# answer = 0

# if len(stair) <= 2:
#     answer = sum(stair)
# else:
#     dp[0] = stair[0]
#     dp[1] = stair[0] + stair[1]
#     for i in range(2, n):
#         dp[i] = max((dp[i - 3] + stair[i - 1] + stair[i]), 
#                     (dp[i - 2] + stair[i]))
#     answer = dp[n - 1]


# print(answer)
li = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(li[0])
print(li[-1])