N, K = map(int, input().split())
coins = []
coin_cnt = 0
coin_sum = 0
for _ in range(N):
    coins.insert(0,int(input()))

for coin in coins:
    coin_cnt += K//coin
    K %= coin
    if not K:   
        break
    else :
        continue
print(coin_cnt)