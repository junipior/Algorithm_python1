# 7월 11일
# 가장 큰 수

# 1
def solution(num):
    num = list(map(str, num)) # 각각 요소를 int가 아닌 str로 바꾸기
    num.sort(key = lambda x : x*3, reverse = True) # 참고
    return str(int(''.join(num)))
# input
# [9, 7, 5, 50, 70, 700, 900, 91]

# output
# "991900770700550"

# 참고
# 만약 '9', '900', '91'이 있을 때 ASCII 코드로 확인해 보면
# ord('0') = 48, ord('1') = 49, ord('9') = 57
# x * 3 했을 때 기준으로 아스키가 큰 순으로 나열 하는 것이니깐
# '99/9' (57 57) , '90/0900900' (57 / 48) , '91/ 9191' (57 49) (* 같다면 다음 수 까지 비교)
# 따라서 9 900 91 순이다.


# 2 - 시간 초과/ 순열의 경우 시간 복잡도 O(n!)

# from itertools import permutations
# from functools import reduce
# def solution(numbers):
#     num = list(permutations(numbers, len(numbers)))
#     num_to_str = [reduce(lambda x,y: str(x) + str(y), i) for i in num]
#     return max(num_to_str)