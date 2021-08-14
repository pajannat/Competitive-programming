from sys import stdin
input = stdin.readline

N = int(input())
coin_list = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
coin_list.sort(reverse=True)

coin_num = 0
coin_nokori = N
for coin in coin_list:
    coin_num += coin_nokori // coin
    coin_nokori = coin_nokori - (coin_nokori // coin)*coin

print(coin_num)
