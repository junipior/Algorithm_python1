# 6월 24일
# 프로그래머스 해쉬
# 완주하지 못한 선수

# 1
def solution(participant, completion):
    temp = 0
    dic = dict()
    for part in participant:
        dic[hash(part)] = part # hash(part)값이 key값이고 part가 value인 사전 자료형 생성
        temp += hash(part) # temp에 고유값인 part의 해쉬값을 모두 저장.
    for com in completion:
        temp -= hash(com) # 집합에서 차집합과 유사하게 사용
    answer = dic[temp]

    # return answer 프로그래머스
    print("\""+answer+"\"")

# input
solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])

# output
# 'mislav'

# 2
# Counter 이용

# from collections import Counter
# def solution(participant, completion):
#     answer = Counter(participant) - Counter(completion)
#     return list(answer.keys())[0]

