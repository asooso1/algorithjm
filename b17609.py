def palindrome(in_str): # 회문체크
    
    if in_str == in_str[::-1]:
        return True
    else :
        return False


for tc in range(int(input())):
    string = list(input())
    answer = palindrome(string)
    if answer:
        print(0)
    else:
        i = 0
        while i<len(string)//2:
            if string[i] == string[-(i+1)]: # 양끝에서 한칸씩 비교해서 다를 경우의 인덱스를 이용
                pass
            else:                           # 다른 두 글자를 각각 빼서 회문체크
                str1 = string[:]        
                str1.pop(i)
                str2 = string[:]
                str2.pop(-(i+1))
                if palindrome(str1) or palindrome(str2):
                    print(1)
                else:
                    print(2)
                break
            i += 1