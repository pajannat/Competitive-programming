def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N, M = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    ans = list(A - B)
    ans.sort()
    
    # 出力
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()