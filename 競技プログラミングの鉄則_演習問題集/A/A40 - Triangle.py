def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    bar = [0] * 101
    ans = 0

    # 処理
    for a in A:
        bar[a] += 1
    
    for num in bar:
        if num < 3:
            continue

        ans += cmb(num, 3)
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()