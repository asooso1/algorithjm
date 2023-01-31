city = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))
answer = 0
min_price = price[0]

for i in range(city-1):
    if min_price > price[i]:     # 다음 도시에서 전 도시까지의 최소값이 저렴하면 비용 합산
        min_price = price[i]
    answer += min_price * distance[i]
print(answer)