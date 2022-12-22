def palindrome(text):
    for i in range(len(text)//2):
        if text[i] == text[-(i+1)]:
            continue
        else :
            return 0
    return 1
T = int(input())
for test_case in range(1,T+1):
    test_text = input()
    print(f'#{test_case} {palindrome(test_text)}')