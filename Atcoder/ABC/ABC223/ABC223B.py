def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = input().rstrip()

    A = []
    for i in range(len(S)):
        A.append(S[i:]+S[:i])
    A.sort()

    print(A[0])
    print(A[-1])

if __name__ == '__main__':
    main()