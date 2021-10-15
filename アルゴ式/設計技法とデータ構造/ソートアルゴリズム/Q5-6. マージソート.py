def main():
    from sys import stdin
    input = stdin.readline

    import collections
    import sys

    # スタックオーバーフローを防ぐ
    sys.setrecursionlimit(int(1E+5))

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))

    def mergesort(list):
        X = len(list) // 2
        L = []
        R = []
        if len(list) == 2:
            L.append(list[0])
            R.append(list[1])
        else:
            for i in range(len(list)):
                if i <= X:
                    L.append(list[i])
                else:
                    R.append(list[i])
        
        if len(L) > 1:
            L = mergesort(L)

        if len(R) > 1:
            R = mergesort(R)

        LR = collections.deque(L+R[::-1])
        B = []

        while LR:
            if len(LR) <= 1:
                B.append(LR[0])
                break

            if LR[0] <= LR[-1]:
                B.append(LR.popleft())
            else:
                B.append(LR.pop())
        
        return B

    print(*mergesort(A))

if __name__ == '__main__':
    main()