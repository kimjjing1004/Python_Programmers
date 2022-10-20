# https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3

def solution(n):
    answer=''
    for i in range(2,n+1,2):
        answer+='수박'

    if n%2==1:
        answer+='수'

    else:
        pass

    return answer


print(solution(3))  # 수박수
print(solution(4))  # 수박수박
