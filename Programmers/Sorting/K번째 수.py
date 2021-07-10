# 7월 10일
# 프로그래머스 정렬(Sorting)
# 보트는 최대 "2명"이 탈 수 있음

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]
        sel = commands[i][2] - 1
        lst = array[start:end]
        lst.sort()
        num = lst[sel]
        answer.append(num)
    return answer

#a rray	commands	return
# [1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]