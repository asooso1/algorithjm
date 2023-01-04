import sys
sys.stdin = open('1928_input.txt','r')

def base64_decoder(char):
    if char.isupper():
        return str(bin(ord(char) % 65))[2:]
    elif char.islower():
        return str(bin(ord(char) % 97 + 26))[2:]
    elif char.isdigit():
        return str(bin(int(char)+52))[2:]
    else :
        if char == '+':
            return str(bin(62))[2:]
        else :
            return str(bin(63))[2:]

T = int(input())

for test_case in range(1,T+1):
    input_str = input()
    answer = ''
    decoding_bin_str = ''
    for idx,char in enumerate(input_str):
        temp_str = base64_decoder(char) # 문자 하나를 받아서 6bit 문자열로 변환
        while len(temp_str) < 6: 
            temp_str = '0' + temp_str
        decoding_bin_str += temp_str
        if idx % 4 == 3:    # 6bit 문자열 4개가 합쳐질 때마다 8bit 3개로 쪼개서 아스키 코드 변환
            for i in range(3):
                temp_char = chr(int(decoding_bin_str[i * 8 : (i + 1) * 8],2))
                answer += temp_char
            decoding_bin_str = ''
    print(f'#{test_case} {answer}')