def main():
    from sys import stdin
    input = stdin.readline
    N = int(input())

    # 数値として入力一つを読み込み
    N = int(stdin.readline().rstrip())
    # 文字列を読み込み。末尾の改行は取り、空白で分割。
    A = stdin.readline().rstrip().split()
    # 数値列として読み込み。末尾の改行は取り、空白で分割。
    A = [int(i) for i in stdin.readline().rstrip().split()]
    # 複数行読み込み
    A = [int(i.rstrip()) for i in stdin.readlines()]
    # n×m行列の入力を2次元リストに格納
    INPUT = [[]*m for _ in range(n)]
    for idx in range(n):
        INPUT[idx] = [int(i) for i in input().split()]


if __name__ == '__main__':
    main()