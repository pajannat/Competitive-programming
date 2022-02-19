def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    kireme = []

    # 12 時の方向に切れ込みを入れる
    kireme.append(0)
    kireme.append(360)  

    kaiten = 0
    for a in A:
        kaiten = (kaiten+a)%360
        if kaiten not in kireme:
            kireme.append(kaiten)
    
    kireme.sort()
    
    chushinkaku = []
    L = len(kireme)
    for i in range(L-1):
        chushinkaku.append(abs(kireme[i+1]-kireme[i]))

    # print(kireme)
    # print(chushinkaku)
    print(max(chushinkaku))

if __name__ == '__main__':
    main()
