def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    for i in range(M):
        if B[i] in A:
            A.remove(B[i])
            cnt += 1

    if cnt == M:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()