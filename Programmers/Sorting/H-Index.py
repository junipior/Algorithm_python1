# 7월 12일
# 가장 큰 수

# 1
# def solution(citations):
#     citations.sort()
#     n = len(citations)
#     lst = []
#     answer = 0
#     for num in range(n + 1):
#         cnt = 0
#         for cit in citations:
#             if num <= cit:
#                 cnt += 1
#         lst.append(cnt)
#         if lst[num] >= num:
#             answer = num
#     return answer

# 2

def solution(citations):
  sorted_citations = sorted(citations, reverse=True)
  n = len(sorted_citations)
  for i in range(n):
    if sorted_citations[i] <= i:
      return i
  return len(sorted_citations)

# 3

# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer

print(solution([3, 0, 6, 1, 5])) # 3
print(solution([88, 89]))  # 2
print(solution([1, 4])) # 1
print(solution([3, 0, 1, 2])) # 2