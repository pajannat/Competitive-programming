import io
import sys

_INPUT = """\
47
S 10
S 11
S 12
S 13
H 1
H 2
S 6
S 7
S 8
S 9
H 6
H 8
H 9
H 10
H 11
H 4
H 5
S 2
S 3
S 4
S 5
H 12
H 13
C 1
C 2
D 1
D 2
D 3
D 4
D 5
D 6
D 7
C 3
C 4
C 5
C 6
C 7
C 8
C 9
C 10
C 11
C 13
D 9
D 10
D 11
D 12
D 13
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    from sys import stdin
    input = stdin.readline
    
    n = int(input())

    S_set = set()
    H_set = set()
    C_set = set()
    D_set = set()

    def SetAdd(mark):
        if mark == "S":
            S_set.add(num)
        elif mark == "H":
            H_set.add(num)
        elif mark == "C":
            C_set.add(num)
        elif mark == "D":
            D_set.add(num)

    for _ in range(n):
        mark, num = input().split()
        num = int(num)
        
        SetAdd(mark)

    mark_list = ["S","H","C","D"]
    set_list = [S_set,H_set,C_set,D_set]
    for mark,mark_set in zip(mark_list,set_list):
        for idx in range(1,14):
            if idx in mark_set:
                pass
            else:
                print(mark,idx) 
    
if __name__ == '__main__':
    main()







