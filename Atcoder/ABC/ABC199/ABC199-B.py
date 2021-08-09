import io
import sys

_INPUT = """\
100 50 4

"""
sys.stdin = io.StringIO(_INPUT)


#------以下にコードを記述-----
def main():
    from sys import stdin
    input = stdin.readline
    N = int(input())
    A_list = [int(i) for i in input().split()]
    B_list = [int(i) for i in input().split()]
    
    num_min = max(A_list)
    num_max = min(B_list)
    
    if num_max-num_min+1 >=0:
        print(num_max-num_min+1)
    else:
        print(0)

if __name__ == '__main__':
    main()