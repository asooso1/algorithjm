def solution(numbers, hand):
    ans = ''
    left_list = [1,4,7]
    right_list = [3,6,9]
    left = 10                   # *은 10번
    right = 12                  # #은 12번
    for number in numbers:
        if number == 0:         # 0은 11번
            number += 11
        if number in left_list :
            ans += 'L'
            left = number
        elif number in right_list :
            ans += "R"
            right = number
        else :
            if abs(number - right) // 3 + abs(number - right) % 3 > abs(number - left) % 3 + abs(number - left) // 3:
                ans += 'L'
                left = number
            elif abs(number - right) // 3 + abs(number - right) % 3 < abs(number - left) % 3 + abs(number - left) // 3:
                ans += 'R'
                right = number
            else :
                if hand == 'right' :
                    ans += 'R'
                    right = number
                else :
                    ans += 'L'
                    left = number
            
    return ans