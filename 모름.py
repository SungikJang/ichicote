pay = int(input())

def CalculateCoin(payment):
    coin500 = 0
    coin100 = 0
    coin50 = 0
    coin10 = 0
    count = 0
    left = payment
    while left > 0:
        if left >= 500:
            coin500 = payment // 500
            left = left - coin500 * 500
            print(coin500, left)
        if left >=100 & left < 500:
            coin100 = left // 100
            left = left - coin100 * 100
            print(coin100, left)
        if left >= 50 & left < 100:
            coin50 = left // 50
            left = left - coin50 * 50
            print(coin50, left)
        if left < 50:
            coin10 = left // 10
            left = left - coin10 * 10
            print(coin10, left)
    resultpay = (coin10,coin50,coin100,coin500)
    for coin in resultpay:
        count += coin
    return count



result = CalculateCoin(pay)

print (result)
# 너무 오지게 길게풀음

coins = (500,100,50,10)
count = 0
for coin in coins:
    count +=(pay // coin)
    pay %= coin

print (count)

#개 짧아짐; 나바보 멍청이 등신