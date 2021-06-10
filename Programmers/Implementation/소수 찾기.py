# 6월 10일
# 프로그래머스 구현
# 소수 찾기

from itertools import permutations # 순열 구하기 위해

def prime_number(n):
    if n >= 2:
        for i in range(2, n):
            if n%i == 0: # 2이상 n미만의 수로 나누어떨어지면 소수가 아님
                return False
        return True # 나누어 떨어지지 않을 때 True 반환
    else:
        return False # n이 1이면 소수가 아니므로 False

def solution(numbers):
    lst = []
    for i in range(1, len(numbers)+1):
        lst.append(list(map(''.join, permutations(numbers, i)))) # 모든 순열 조합 구해서 lst 변수에 저장
    lst = sum(lst, []) # 다차원 리스트(이중이상의 리스트) 일 경우 하나로 합치기
    lst = list(set(map(int, lst))) # 중복제거하고 정수로 바꾸고(011 같은 숫자 자동 제거됨) 다시 리스트화
    answer = 0
    for k in lst:
        if prime_number(k) == True: # 소수이면 카운트 1추가
            answer += 1
    return answer