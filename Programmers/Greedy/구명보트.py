# 7월 9일
# 프로그래머스 그리디(Greedy)
# 보트는 최대 "2명"이 탈 수 있음

def solution(people, limit):
    people.sort()
    cnt = 0
    start = 0
    end = len(people) - 1
    while start <= end:
        cnt += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
    return cnt

# solution([70, 50, 80, 50]	100)
# 3