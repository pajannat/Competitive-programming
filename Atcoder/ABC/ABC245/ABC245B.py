def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = set(list(map(int, input().split())))

    for i in range(2001):
        if i in A:
            pass
        else:
            print(i)
            break

if __name__ == '__main__':
    main()