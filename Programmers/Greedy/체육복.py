# 7월 6일
# 프로그래머스 그리디(Greedy)
# 체육복
def solution(n, lost, reserve):
    set_lost = sorted([l for l in lost if l not in reserve]) # 보유하지도 않고 잃어버린 학생
    set_reserve = sorted([r for r in reserve if r not in lost]) # 보유했는데 잃어버리지 않은 학생 ( 보유했는데 잃어버리면 체육복을 하나 가진 걸로 가정)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    answer = n - len(set_lost)
    return answer

# solution(7, [2, 4, 6], [3, 5, 2, 4])
# 7