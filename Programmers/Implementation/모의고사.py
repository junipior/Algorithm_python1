# 6월 10일
# 프로그래머스 구현
# 모의고사
# 가장 문제를 많이 맞힌 사람 구하기

from itertools import cycle

def solution(answers):
    winner = []
    pattern_supo_1 = [1, 2, 3, 4, 5]
    pattern_supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score_supo = [0, 0, 0]

    for supo_1, supo_2, supo_3, answer in zip(cycle(pattern_supo_1), cycle(pattern_supo_2), cycle(pattern_supo_3),
                                              answers): # 가장 길이가 긴 것을 기준으로 반복 ex) 최소 리스트 길이가 3이면 모두 길이가 3까지만 반복
        if supo_1 == answer: score_supo[0] += 1
        if supo_2 == answer: score_supo[1] += 1
        if supo_3 == answer: score_supo[2] += 1

    for i, score in enumerate(score_supo):
        if score == max(score_supo):
            winner.append(i + 1)

    return winner

solution([1, 2, 3, 4, 5])

# input
# answer = [1,2,3,4,5]

# output
# [1]