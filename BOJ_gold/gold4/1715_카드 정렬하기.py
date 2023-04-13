import sys
import heapq
input = sys.stdin.readline

n = int(input())
answer = 0
card = []
for i in range(0, n):
    heapq.heappush(card, int(input()))

while len(card) > 1:
    tmp = heapq.heappop(card)
    tmp += heapq.heappop(card)
    answer += tmp
    heapq.heappush(card, tmp)

print(answer)

