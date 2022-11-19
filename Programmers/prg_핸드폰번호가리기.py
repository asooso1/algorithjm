def solution(phone_number):
    answer = ''
    for idx in range(len(phone_number)-4):
        answer += '*'
    answer += phone_number[-4:]
    return answer