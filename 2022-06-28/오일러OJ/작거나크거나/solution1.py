# https://euleroj.io/problemset/editor/1001

def solution(A, B):
    answer = ''

    if A > B:
        answer = '>'
    elif A == B:
        answer = '='
    elif A < B:
        answer = '<'

    print(answer)


solution(200009, 90)  # '>'
