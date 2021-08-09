import io
import sys

_INPUT = """\
3 10
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    from sys import stdin
    # 数値として入力一つを読み込み
    N, K = map(int, stdin.readline().split())
    
    import math
    sum = 0
    for i in range(1,N+1):
        if i >= K:
            sum += (1/N)
        else:
            n = math.ceil(math.log2(K/i))
            sum += pow(2,-n)/N
    print(sum) 


if __name__ == '__main__':
    main()