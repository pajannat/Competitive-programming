import io
import sys

_INPUT = """\
3
1 1 3 8
3 2 2 7
4 3 8 1
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    from sys import stdin
    input = stdin.readline
    
    n = int(input())
    INPUT = [[]*4 for _ in range(n)]
    for idx in range(n):
        INPUT[idx] = [int(i) for i in input().split()]

    off1 = [[0]*10 for _ in range(3)]
    off2 = [[0]*10 for _ in range(3)]
    off3 = [[0]*10 for _ in range(3)]
    off4 = [[0]*10 for _ in range(3)]

    off_list = [off1,off2,off3,off4]

    for inp in INPUT:
        b = inp[0]
        f = inp[1]
        r = inp[2]
        v = inp[3]

        off_list[b-1][f-1][r-1] += v

    for idx, off in enumerate(off_list):
        for flr in off:
            print("",*flr)
        if idx == len(off_list)-1:
            pass
        else:
            print("####################")
    
if __name__ == '__main__':
    main()







