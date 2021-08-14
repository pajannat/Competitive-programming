def main():
    from sys import stdin
    input = stdin.readline

    A,B,C = map(int,input().split())
    if (A == 0) and (B == 0):
        print("=")
    elif abs(A) > abs(B):
        if (A > 0) and (B > 0):
            print(">")
        elif (A > 0) and (B < 0):
            print(">")
        elif (A < 0) and (B > 0):
            if C % 2 == 0:
                print(">")
            else:
                print("<")
        elif (A < 0) and (B < 0):
            if C % 2 == 0:
                print(">")
            else:
                print("<")
        elif (A > 0) and (B == 0):
            print(">")
        elif (A < 0) and (B == 0):
            if C % 2 == 0:
                print(">")
            else:
                print("<")
    elif abs(A) < abs(B):
        if (A > 0) and (B > 0):
            print("<")
        elif (A > 0) and (B < 0):
            if C % 2 == 0:
                print("<")
            else:
                print(">")
        elif (A < 0) and (B > 0):
            print("<")
        elif (A < 0) and (B < 0):
            if C % 2 == 0:
                print("<")
            else:
                print(">")
        elif (A == 0) and (B > 0):
            print("<")
        elif (A == 0) and (B < 0):
            if C % 2 == 0:
                print("<")
            else:
                print(">")
    elif abs(A) == abs(B):
        if (A > 0) and (B > 0):
            print("=")
        elif (A > 0) and (B < 0):
            if C % 2 == 0:
                print("=")
            else:
                print(">")
        elif (A < 0) and (B > 0):
            if C % 2 == 0:
                print("=")
            else:
                print("<")
        elif (A < 0) and (B < 0):
            print("=")


if __name__ == '__main__':
    main()