def solution(n):
    answer = 0
    list_n = []
    str_n = ''
    while n!=0:
        list_n.append(n % 10)
        n //= 10
    list_n.sort()
    list_n.reverse()
    for i in list_n:
        str_n += str(i)
    answer = int(str_n)
    return answer