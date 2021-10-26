def main():
    from sys import stdin
    input = stdin.readline

    import random

    N = int(input())
    A = list(map(int, input().split()))

    def random_quicksort(list):
        # 空配列の場合はなにもせず終了
        if len(list) <= 1:
            return list
        
        X = random.randint(0, len(list)-1)
        L = []
        M = [list[X]]
        R = []
        for i in range(len(list)):
            if i != X:
                if list[i] < list[X]:
                    L.append(list[i])
                elif list[i] > list[X]:
                    R.append(list[i])
                else:
                    M.append(list[i])
        return random_quicksort(L) + M + random_quicksort(R)
    
    # 出力
    print(*random_quicksort(A))

if __name__ == '__main__':
    main()