def main():
    from sys import stdin
    input = stdin.readline

    import itertools
    # 入力を受け取る
    N = int(input())

    ans = []

    # R桁のbit全探索
    R = N
    from itertools import product
    P = product((0, 1), repeat=R)

    for p in P:
        res = ""
        tmp = 0
        for i in p:
            if i == 1:
                res += "("
                tmp += 1
            else:
                res += ")"
                tmp -= 1
            if tmp < 0:
                break
        if tmp == 0:
            ans.append(res)
    
    ans.sort()

    for a in ans:
        print(a)
    
if __name__ == '__main__':
    main()