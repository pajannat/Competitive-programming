def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    shift = 0

    for i in range(Q):
        T, x, y = map(int, input().split())
        x_idx = (x - 1 - shift) % N
        y_idx = (y - 1 - shift) % N

        if T == 1:
            A[x_idx], A[y_idx] = A[y_idx], A[x_idx]
        elif T == 2:
            shift += 1
        elif T == 3:
            print(A[x_idx])

if __name__ == '__main__':
    main()