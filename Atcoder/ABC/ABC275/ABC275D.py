def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    from functools import lru_cache  
    @lru_cache(maxsize=None)
    def f(num):
        if num == 0:
            return 1
        elif num > 0:
            return f(num//2) + f(num//3)

    # 答えを出力
    print(f(N))


if __name__ == '__main__':
    main()