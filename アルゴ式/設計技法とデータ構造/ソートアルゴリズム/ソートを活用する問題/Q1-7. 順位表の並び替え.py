def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N = int(input())

    A = []
    for i in range(N):
        s, a, b = input().split()
        a = int(a)
        b = int(b)
        A.append([s, a, b, a+b])
    
    A.sort(key=lambda x: x[3])
    A.sort(key=lambda x: x[1], reverse=True)

    # 出力
    for s, a, b, _ in A:
        print(s, a, b)

if __name__ == '__main__':
    main()