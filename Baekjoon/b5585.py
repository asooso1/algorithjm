price = int(input())
coins = [500, 100, 50, 10, 5, 1]
change = 1000 - price
cnt = 0
for coin in coins:
    cnt += change // coin
    change %= coin

print(cnt)