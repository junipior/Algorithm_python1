# 7월 10일
# 프로그래머스 정렬(Sorting)
# A.sort()는 리스트를 그 자리에서 정렬하고 None을 반환

# 1
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

# 2

def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]

# 3

def solution(array, commands):
    return list(map(lambda x : sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# answer
# array	commands return
# [1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]