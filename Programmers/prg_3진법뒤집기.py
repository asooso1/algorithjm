def solution(n):
    answer = 0
    string = ''
    while n > 0 :
        string += str(n % 3)
        n //= 3

    for i in range(len(string)):
        answer += (int(string[i]) % 3) * (3 ** (len(string)-i-1))
    return answer
print(solution(45))