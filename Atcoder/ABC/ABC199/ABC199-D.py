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
    A,B = map(int,input().split())


    for num in range(1,N+1):
        if A%num==0 and B%num==0:
            num_list.append(num)

    print(num_list[-K])

if __name__ == '__main__':
    main()