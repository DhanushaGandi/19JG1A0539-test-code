def solution(num):
    s = '-' if num<0 else ''
    num = abs(num)
    if num < 3:
        return str(num)
    ss = ''
    while num != 0:
        ss = str(num%3) + ss
        num = num//3
    return s+ss
num=int(input())
print(solution(num))
