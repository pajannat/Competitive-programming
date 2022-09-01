def main():
    from sys import stdin
    input = stdin.readline

    import numpy
    from itertools import combinations

    def cross_product_ABxAC(ax, ay, bx, by, cx, cy):
        vec_AB = [bx-ax, by-ay]
        vec_AC = [cx-ax, cy-ay]
        return numpy.cross(vec_AB, vec_AC)

    # 入力を受け取る
    Ax, Ay = map(int, input().split())
    Bx, By = map(int, input().split())
    Cx, Cy = map(int, input().split())
    Dx, Dy = map(int, input().split())

    # 処理
    # ABCDから3点選ぶ組み合わせ comb_ABCD
    comb_ABCD = combinations([[Ax, Ay], [Bx, By], [Cx, Cy], [Dx, Dy]], 3)
    for a in comb_ABCD:
        print(a)
    
    # ABCDから1点選ぶ

    # 選んだ1点が他三点からなる三角形に内包されるかを判定
    # 三角形ABCにDが含まれるか判断するには
    # vec_AB, vec_BA, vecCA とAD
    
    # 答えを出力
    print(Ax, Ay)
    print(Bx, By)
    print(Cx, Cy)
    print(Dx, Dy)


if __name__ == '__main__':
    main()