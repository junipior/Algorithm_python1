from collections import deque

## deque는 양방향 삽입이 가능하기 때문에 스택 큐, 데크(양방향 큐)로 사용가능

## Append: list와 deque 모두 우측 삽입

## Appendleft 좌측 삽입 (list는 불가)

## extend (우측 삽입이나 deque에선 하나씩 삽입

deq = (['a', 'b', 'c', 'd'])
deq.extend("apple")
print(deq)
# ['a', 'b', 'c', 'd', 'a', 'p', 'p', 'l', 'e']

deq2 = (['a', 'b', 'c', 'd'])
deq2.append("samsung")
print(deq2)
# ['a', 'b', 'c', 'd', 'samsung']

## extendleft 좌측 삽입 방식은 extend와 동일

## pop 오른쪽에서 부터 제거 list는 인덱스 입력가능.
deq3 = (["x", "y", "z"])
deq3.pop()
print(deq3)

lst = [3,5,8]
lst.pop(1)
print(lst)

## popleft() deque만 가능 좌측에서 제거.

## rotate 회전
# 나만의 방법 : rotate(1)이면 뒤에서 하나 가져와서 앞에 붙힘
# rotate(-3) 이면 앞에서 3개 가져와서 뒤에 붙힘

deq4 = deque(['q', 'w', 'e', 'r', 't', 'y'])
deq4.rotate(-4)
print(deq4)
# deque(['t', 'y', 'q', 'w', 'e', 'r'])
