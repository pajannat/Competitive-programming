import io
import sys

_INPUT = """\
3 3
0 2 6728
2 0 8444
2 1 5955
"""
sys.stdin = io.StringIO(_INPUT)

# 方針：総当たりする
# ① 0~N-1番を並び替えた数値列を全パターン用意
# ② 各数値列に対し得点を計算（各得点パターンに対して計算し、sum）
# ③ 前の数値列より高得点なら、max_scoreパターンとして保持

def main():
    from sys import stdin

    N, M = map(int, stdin.readline().rstrip().split())

    score_list = []
    for i in range(M):
        score_list_tmp = [int(i) for i in stdin.readline().rstrip().split()]
        score_list.append(score_list_tmp)
    
    import itertools
    # 0からN-1までのリスト
    lis = [x for x in range(N)] 
    # 0~N-1の品物の順列の全パターンをリストに格納。
    permutations_lis = list(itertools.permutations(lis))

    # 品物の順列とスコア表を比較
    max_score = 0
    for permutations in permutations_lis:
        sum = 0
        # 数値列のi番目とj番目をスコア表と比較
        for i in range(len(permutations)):
            for j in range(i+1,len(permutations)):
                for k in score_list:
                    if permutations[i]==k[0] and permutations[j]==k[1]:
                        sum += k[2]
        if sum > max_score:
            max_score = sum

    print(max_score)

if __name__ == '__main__':
    main()