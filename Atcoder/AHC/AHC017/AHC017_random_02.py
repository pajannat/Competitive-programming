"""
その日に工事する辺をランダムに選択
工事する辺の数は毎日最大 -> 工事をまとめて行い、後半を工事なしとする作戦

"""

def main():
    from sys import stdin
    input = stdin.readline

    import random

    # 入力を受け取る
    N, M, D, K = map(int, input().split())
    r = [0] * M

    # 処理
    edge = set(range(1, M+1))
    for i in range(1, D+1):
        sample_i = random.sample(edge, min(len(edge), K))
        edge = edge - set(sample_i)
        for j in sample_i:
            r[j-1] = i
    
    # 答えを出力
    print(*r)

    # # 出力確認用コード
    # text = ""
    # for s in r:
    #     text += str(s) + (" ")
    # print(text)
    # with open("./test.txt", "w",encoding="utf_8") as f:
    #     f.write(text)


if __name__ == '__main__':
    main()