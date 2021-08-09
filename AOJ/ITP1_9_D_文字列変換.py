import io
import sys

_INPUT = """\
abcdefghij
15
reverse 3 7
print 1 8
replace 1 3 xyz
print 1 8
replace 4 6 fff
print 1 8
replace 5 5 o
print 1 8
reverse 3 7
print 1 8
replace 8 9 xy
print 0 9
reverse 3 8
reverse 0 5
print 0 9
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    from sys import stdin
    input = stdin.readline
    S = list(input().rstrip())
    n = int(input())
    line_list = [i.rstrip().split() for i in stdin.readlines()]

    for line in line_list:
        if line[0] == "print":
            print(*S[int(line[1]):int(line[2])+1],sep="")
        elif line[0] == "reverse":
            S_tmp = S.copy()
            for idx in range(int(line[1]),int(line[2])+1):
                S[idx] = S_tmp[int(line[2])-(idx-int(line[1]))]
        elif line[0] == "replace":
            S_tmp = S.copy()
            cnt = 0
            for idx in range(int(line[1]),int(line[2])+1):
                S[idx] = line[3][cnt]
                cnt += 1

if __name__ == '__main__':
    main()