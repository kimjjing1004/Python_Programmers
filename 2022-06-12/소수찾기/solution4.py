# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = []
    x = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if x[i]:
            answer.append(i)

            for j in range(2 * i, n + 1, i):
                x[j] = False

    return len(answer)

# 에리토스테네스의 체로 구현한 코드 (뭔 소린지 1도 모름)
# n값이 늘어 날 수록 이전 solution3 코드와 많은 시간 차이가 생긴다
# 효용성 테스트 모두 성공...
# https://inten.tistory.com/entry/Python-3x-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%86%8C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0


print(solution(10))  # 4 [2, 3, 5, 7]
print(solution(5))  # 3 [2, 3, 5]
