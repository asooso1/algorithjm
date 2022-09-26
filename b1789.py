N = int(input())
number = 1
total = 0
cnt = 0

while True:
    cnt += 1
    total += number
    if (N - total) <= number:
        break
    else:
        number += 1

print(cnt)