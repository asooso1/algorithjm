T = int(input())
for i in range(T):
    input_str = input()
    a, b = input_str.split(' ')
    ans1, ans2 = divmod(int(a), int(b))
    print(f'#{i+1} {ans1} {ans2}')