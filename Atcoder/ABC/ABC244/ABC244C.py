def main():
    import sys
    input = sys.stdin.readline

    # 入力を受け取る
    N = int(input())

    set_N = set(range(1, 2*N+2))

    for i in range(1, 2*N+2):
        takahashi_ans = set_N.pop()
        print(takahashi_ans)
        sys.stdout.flush()

        aoki_ans = int(input())
        sys.stdout.flush()

        if aoki_ans == 0:
            break
        else:
            set_N.remove(aoki_ans)

if __name__ == '__main__':
    main()