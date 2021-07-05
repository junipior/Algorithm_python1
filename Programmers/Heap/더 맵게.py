# 7월 5일
# 프로그래머스 힙(Heap)
# 더 맵게
# from heapq import heappop, heappush, heapify 사용

def solution(scoville, K):
    from heapq import heappop, heappush, heapify
    answer = 0
    total = 0
    heapify(scoville)
    while scoville[0] < K:
        first = heappop(scoville)
        second = heappop(scoville)
        total = first + (2 * second)
        answer += 1
        heappush(scoville,total)
        if (len(scoville) <= 2) & (total < K):
            return -1
    return answer

# input
# scoville	K	return
# [1, 2, 3, 9, 10, 12]	7	2