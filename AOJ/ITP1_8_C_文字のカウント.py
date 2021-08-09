import io
import sys

_INPUT = """\
This is a pen.
Hello World.
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    from sys import stdin
    input = stdin.readlines

    mydict = {}
    for i in range(ord('a'),ord('z')+1):
        mydict[chr(i)] = 0
    
    S = [i.rstrip().lower() for i in input()]

    for sentence in S:
        for x in sentence:
            if x in mydict:
                mydict[x] += 1

    for i in mydict:
        print("{0} : {1}".format(i,mydict[i]))        

if __name__ == '__main__':
    main()