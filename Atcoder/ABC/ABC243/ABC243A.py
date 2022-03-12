def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    V, A, B, C = map(int, input().split())

    for i in range(10**5+5):
        if V-A < 0:
            print("F")
            break
        V -= A

        if V-B < 0:
            print("M")
            break
        V -= B

        if V-C < 0:
            print("T")
            break
        V -= C

if __name__ == '__main__':
    main()