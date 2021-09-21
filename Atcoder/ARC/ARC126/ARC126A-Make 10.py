def main():
    from sys import stdin
    input = stdin.readline

    T = int(input())
    N_list =[]
    for _ in range(T):
        N2, N3, N4 = map(int, input().split())
        N_list.append([N2, N3, N4])
    
    def Test(N2, N3, N4):
        cnt_10 = 0
        N2_remain = N2
        N3_remain = N3
        N4_remain = N4

        # 長さ3の棒2本と、長さ4の棒で10を作る
        n2 = 0
        n3 = 0
        n4 = 0

        n3 = N3_remain // 2
        N3_remain -= n3*2
        if n3 > 0:
            if N4_remain >= n3:
                n4 = n3
                N4_remain -= n3
            else:
                n4 = N4_remain
                N4_remain -= n4

            # 長さ3の棒とのペアを組むのに、長さ4の棒だけでは足りないとき長さ2の棒も使う
            if (n3-n4) <= 0:
                pass
            else:
                if N2_remain >= 2*(n3-n4):
                    n2 = n3-n4
                    N2_remain -= 2*n2
                else:
                    n2 = N2_remain // 2
                    N2_remain -= 2*n2
        
        # 10の棒を作れた分だけcnt_10に加算
        cnt_10 += (n4 + n2)

        # 長さ4の棒2本と、長さ2の棒1本で10を作る
        n2 = 0
        n3 = 0
        n4 = 0

        n4 = N4_remain // 2
        N4_remain -= n4*2
        if n4 > 0:
            if N2_remain >= n4:
                n2 = n4
                N2_remain -= n2
            else:
                n2 = N2_remain
                N2_remain -= n2

        # 10の棒を作れた分だけcnt_10に加算
        cnt_10 += n2

        # 長さ4の棒の残りと、長さ2の棒で10を作る
        n2 = 0
        n3 = 0
        n4 = 0

        if N4_remain == 1:
            n4 = 1
            N4_remain -= 1
        
            if N2_remain >= 3:
                n2 = 1
                N2_remain -= 3
        
        # 10の棒を作れた分だけcnt_10に加算
        cnt_10 += n2

        # 長さ2の棒で10を作る
        n2 = 0
        n3 = 0
        n4 = 0

        n2 = N2_remain // 5
        N2_remain -= n2

        # 10の棒を作れた分だけcnt_10に加算
        cnt_10 += n2

        print(int(cnt_10))

    for i in range(T):
        N2 = N_list[i][0]
        N3 = N_list[i][1]
        N4 = N_list[i][2]
        Test(N2, N3, N4)

if __name__ == '__main__':
    main()