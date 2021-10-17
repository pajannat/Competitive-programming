def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))

    D = {}
    for a in A:
        if a not in D.keys():
            D.update({a : 1})

            if a-1 not in D.keys():
                D.update({a-1 : 1})
            else:
                D.update({a-1 : D[a-1]+1})

            if a+1 not in D.keys():
                D.update({a+1 : 1})
            else:
                D.update({a+1 : D[a+1]+1})

        else:
            D.update({a : D[a]+1})

            if a-1 not in D.keys():
                D.update({a-1 : 1})
            else:
                D.update({a-1 : D[a-1]+1})

            if a+1 not in D.keys():
                D.update({a+1 : 1})
            else:
                D.update({a+1 : D[a+1]+1})

    ans = - 1
    for d in D:
        ans = max(ans, D[d])

    print(ans)

if __name__ == '__main__':
    main()