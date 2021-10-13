def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    def quicksort(list):
        # 空配列の場合はなにもせず終了
        if len(list) == 0:
            return list

        X = len(list) // 2
        L = []
        R = []
        for i in range(len(list)):
            if i != X:
                if list[i] < list[X]:
                    L.append(list[i])
                else:
                    R.append(list[i])
        return quicksort(L) + [list[X]] + quicksort(R)
    
    # 出力
    print(*quicksort(A))

if __name__ == '__main__':
    main()