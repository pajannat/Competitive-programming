from enum import Enum
from typing import List
import sys


class Pos:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x


class Response(Enum):
    NOT_BROKEN = 0
    BROKEN = 1
    FINISH = 2
    INVALID = -1


class Field:

    def __init__(self, N: int, C: int):
        self.C = C
        self.is_broken = [[False] * N for _ in range(N)]
        self.total_cost = 0

    def query(self, y: int, x: int, power: int) -> Response:
        self.total_cost += power + self.C
        print(f"{y} {x} {power}", flush=True)
        res = Response(int(input()))
        if res in (Response.BROKEN, Response.FINISH):
            self.is_broken[y][x] = True
        return res


class Solver:

    def __init__(self, N: int, source_pos: List[Pos], house_pos: List[Pos], C: int, P: int, house_joint_indices: List, MST_min_source: Pos):
        self.N = N
        self.source_pos = source_pos
        self.source_pos_org = source_pos[:]
        self.house_pos = house_pos
        self.house_pos_org = house_pos[:]
        self.C = C
        self.P = P
        self.field = Field(N, C)
        self.field_org = Field(N, C)
        self.house_joint_indices = house_joint_indices
        self.MST_min_source = MST_min_source


    def solve1_test(self):
        solve1_dist_sum = 0
        self.source_pos = self.source_pos_org[:]
        self.house_pos = self.house_pos_org[:]

        # 水源を1つ含めたManhattan_MST を考える
        self.house_pos.append(self.MST_min_source)

        # house_pos (houseとsource 1つ) について Manhattan MST となるようにつなぐ
        for indices in self.house_joint_indices:
            solve1_dist_sum += self.move_test(self.house_pos[indices[0]], self.house_pos[indices[1]])

        return solve1_dist_sum

    def solve2_test(self):
        solve2_dist_sum = 0
        self.source_pos = self.source_pos_org[:]
        # それぞれの houceから, 最も近い水源へ進む
        for house in self.house_pos:
            source = min_Manhattan_dist_source(house, self.source_pos)
            solve2_dist_sum += self.move_test(house, source)

        return solve2_dist_sum

    def move_test(self, start: Pos, goal: Pos):
        # you can output comment
        print(f"# move from ({start.y},{start.x}) to ({goal.y},{goal.x})")

        destructed_field_list = []
        cnt = 0

        # down/up
        if start.y < goal.y:
            for y in range(start.y, goal.y, 1):
                cnt += 1
                destructed_field_list.append([y, start.x])
        else:
            for y in range(start.y, goal.y, -1):
                cnt += 1
                destructed_field_list.append([y, start.x])

        # right/left
        if start.x < goal.x:
            for x in range(start.x, goal.x + 1, 1):
                cnt += 1
                destructed_field_list.append([goal.y, x])
        else:
            for x in range(start.x, goal.x - 1, -1):
                cnt += 1
                destructed_field_list.append([goal.y, x])
        
        # 水源到達時には、破壊した岩盤すべてに水が流れている
        # 破壊した岩盤すべてを水源に追加する
        for destructed_field in destructed_field_list:
            y, x = destructed_field[0], destructed_field[1]
            self.source_pos.append(Pos(y, x))
        
        return cnt

    def solve(self):
        if self.solve1_test() < self.solve2_test():
            self.solve1()
        else:
            self.solve2()

    def solve1(self):
        self.source_pos = self.source_pos_org[:]
        self.house_pos = self.house_pos_org[:]

        # 水源を1つ含めたManhattan_MST を考える
        self.house_pos.append(self.MST_min_source)

        # house について Manhattan MST となるようにつなぐ
        for indices in self.house_joint_indices:
            self.move(self.house_pos[indices[0]], self.house_pos[indices[1]])

        # should receive Response.FINISH and exit before entering here
        raise AssertionError()

    def solve2(self):
        self.source_pos = self.source_pos_org[:]
        # それぞれの houceから, 最も近い水源へ進む
        for house in self.house_pos:
            source = min_Manhattan_dist_source(house, self.source_pos)
            self.move(house, source)

        # should receive Response.FINISH and exit before entering here
        raise AssertionError()

    def move(self, start: Pos, goal: Pos):
        # you can output comment
        print(f"# move from ({start.y},{start.x}) to ({goal.y},{goal.x})")

        now_y = start.y
        now_x = start.x

        down_up_list = []
        right_left_list = []

        destructed_field_list = []

        # down/up
        if start.y < goal.y:
            down_up_list += [1] * abs(goal.y - start.y)
        else:
            down_up_list += [-1] * abs(goal.y - start.y)

        # right/left
        if start.x < goal.x:
            right_left_list += [1] * abs(goal.x - start.x)
        else:
            right_left_list += [-1] * abs(goal.x - start.x)
        
        down_up_list += [0]
        right_left_list += [0]

        move_continue_flg = True
        move_trans_flg = False  # ヨコ移動から開始
        x_None_flg = False
        y_None_flg = False
        bef_destruct_cnt = 5010
        now_destruct_cnt = 5010

        trans_cnt = 0
        trans_continuous_flg = False
        trans_continuous_flg_cnt = 0
        tmp_down_up = 0
        tmp_right_left = 0

        while move_continue_flg:
            if move_trans_flg:
                # タテ移動
                if len(down_up_list) == 0:
                    y_None_flg = True
                    move_trans_flg = False
                else:
                    tmp_down_up = down_up_list.pop()
                    now_y += tmp_down_up
                    now_destruct_cnt = self.destruct(now_y, now_x)
                    # 破壊した岩盤が比較的やわらかい場合は水源として追加
                    if now_destruct_cnt * self.P <= 300:
                        destructed_field_list.append([now_y, now_x])

            else:
                # ヨコ移動
                if len(right_left_list) == 0:
                    x_None_flg = True
                    move_trans_flg = True
                else:
                    tmp_right_left = right_left_list.pop()
                    now_x += tmp_right_left
                    now_destruct_cnt = self.destruct(now_y, now_x)
                    # 破壊した岩盤が比較的やわらかい場合は水源として追加
                    if now_destruct_cnt * self.P <= 300:
                        destructed_field_list.append([now_y, now_x])


            # 岩盤の硬いほうに進んでいる場合はタテヨコ移動を切り替え
            if (now_destruct_cnt > bef_destruct_cnt) and not trans_continuous_flg:
                move_trans_flg = not move_trans_flg
                trans_cnt += 1
            else:
                trans_cnt = 0
            
            # 連続してタテヨコ移動が切り替わっている場合
            # タテヨコ切り替えOFF
            if trans_cnt >= 4:
                trans_continuous_flg = True

            # 数カウント後に trans_continuous_flg : True -> False
            # タテヨコ切り替えをONに戻す
            if trans_continuous_flg:
                trans_continuous_flg_cnt += 1
                if trans_continuous_flg_cnt >= 30:
                    trans_continuous_flg = False
            

            # bef_destruct_cnt の更新
            bef_destruct_cnt = now_destruct_cnt

            # while ループの終了条件の更新
            if x_None_flg and y_None_flg:
                move_continue_flg = False
        
        # 水源到達時には、破壊した岩盤すべてに水が流れている
        # 破壊した岩盤のうちやわらかいもの(S_ij <= 500)を水源に追加する
        for destructed_field in destructed_field_list:
            y, x = destructed_field[0], destructed_field[1]
            self.source_pos.append(Pos(y, x))


    def destruct(self, y: int, x: int):
        # excavate (y, x) with fixed power until destruction
        power = self.P

        destruct_cnt = 0

        while not self.field.is_broken[y][x]:
            destruct_cnt += 1
            result = self.field.query(y, x, power)
            if result == Response.FINISH:
                print(f"total_cost={self.field.total_cost}", file=sys.stderr)
                sys.exit(0)
            elif result == Response.INVALID:
                print(f"invalid: y={y} x={x}", file=sys.stderr)
                sys.exit(1)

        return destruct_cnt


def Manhattan_dist(y1, x1, y2, x2):
    z1 = x1 + y1
    z2 = x2 + y2
    w1 = x1 - y1
    w2 = x2 - y2
    dist = max(abs(z1 - z2), abs(w1 - w2))
    return dist

def min_Manhattan_dist_source(house_pos_i, source_pos):
    min_dist = 1000 # N=200 より, マンハッタン距離は400以下
    min_dist_source = source_pos[0]
    y1 = house_pos_i.y
    x1 = house_pos_i.x

    # house_pos_i から最短距離にある source を全探索で探す
    for source in source_pos:
        y2 = source.y
        x2 = source.x
        tmp_dist = Manhattan_dist(y1, x1, y2, x2)
        if tmp_dist < min_dist:
            min_dist = tmp_dist
            min_dist_source = source

    return min_dist_source


import math
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
from bisect import bisect_left, bisect_right
import sys


class ManhattanMST:
    def __init__(self) -> None:
        self.n = 0
        self.points = []
        self.edges = []

    def add_point(self, i, j):
        self.n += 1
        self.points.append(i)
        self.points.append(j)

    def get_point(self, i):
        return self.points[i << 1 : (i + 1) << 1]

    def sweep(self):
        m = SortedSet()
        d = {}
        for i in self.idx:
            x, y = self.points[i << 1], self.points[(i << 1) + 1]
            while m:
                z = m.le(y)
                if z is None:
                    break
                j = d[z]
                dx = x - self.points[j << 1]
                dy = y - self.points[(j << 1) + 1]
                if dy > dx:
                    break
                self.edges.append((dx + dy, i, j))
                m.discard(z)
                del d[z]
            m.add(y)
            d[y] = i

    def solve(self):
        for i in range(2):
            p_sum = [
                self.points[x << 1] + self.points[(x << 1) + 1] for x in range(self.n)
            ]
            self.idx = sorted(range(self.n), key=lambda x: p_sum[x])
            for _j in range(2):
                self.sweep()
                for j in range(self.n):
                    self.points[j << 1], self.points[(j << 1) + 1] = (
                        self.points[(j << 1) + 1],
                        self.points[j << 1],
                    )
            if not i:
                for j in range(self.n):
                    self.points[j << 1] *= -1
        self.edges.sort(key=lambda x: x[0])
        return self.edges

    def get_mst(self):
        u = UnionFind(self.n)
        for d, i, j in self.solve():
            if u.union(i, j):
                yield d, i, j


class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parent = [-1] * n
        self.groups = n

    def find(self, x: int) -> int:
        if self.parent[x] < 0:
            return x
        else:
            p = x
            while self.parent[p] >= 0:
                p = self.parent[p]
            while self.parent[x] >= 0:
                self.parent[x], x = p, self.parent[x]
            return p

    def union(self, x: int, y: int) -> bool:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.groups -= 1
        return True

    def union_right(self, x: int, y: int) -> bool:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if y > x:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.groups -= 1
        return True

    def union_left(self, x: int, y: int) -> bool:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if x > y:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.groups -= 1
        return True

    def size(self, x: int) -> int:
        return -self.parent[self.find(x)]

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def members(self, x: int) -> list:
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self) -> list:
        return [i for i, x in enumerate(self.parent) if x < 0]

    def group_count(self) -> int:
        return self.groups

    def sizes(self) -> dict:
        return {i: -x for i, x in enumerate(self.parent) if x < 0}

    def all_group_members(self) -> dict:
        from collections import defaultdict

        d = defaultdict(list)
        for i in range(self.n):
            p = self.find(i)
            d[p].append(i)
        return d

    def __str__(self) -> str:
        return "\n".join(
            "{}: {}".format(k, v) for k, v in self.all_group_members().items()
        )


T = TypeVar("T")


class SortedSet(Generic[T]):
    # https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
    BUCKET_RATIO = 75
    REBUILD_RATIO = 255

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None:
            a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [
            a[size * i // bucket_size : size * (i + 1) // bucket_size]
            for i in range(bucket_size)
        ]

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):
            a = sorted(set(a))
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]:
                return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()
        return True

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x:
            return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0:
            self._build()
        return True

    def lt(self, x: T) -> Union[T, None]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Union[T, None]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Union[T, None]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Union[T, None]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0:
            x += self.size
        if x < 0:
            raise IndexError
        for a in self.a:
            if x < len(a):
                return a[x]
            x -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return


def main():
    N, W, K, C = [int(v) for v in input().split(" ")]
    source_pos = []
    house_pos = []

    for _ in range(W):
        y, x = (int(v) for v in input().split(" "))
        source_pos.append(Pos(y, x))
    for _ in range(K):
        y, x = (int(v) for v in input().split(" "))
        house_pos.append(Pos(y, x))
    
    # power を決定する
    if C == 1:
        P = 32
    elif C == 2:
        P = 32
    elif C == 4:
        P = 64
    elif C == 8:
        P = 128
    elif C == 16:
        P = 128
    elif C == 32:
        P = 256
    elif C == 64:
        P = 256
    elif C == 128:
        P = 256

    n = K + 1
    cost = 200 * 200
    house_joint_indices = []
    MST_min_source = None
    for source in source_pos:
        tmp = []
        tmp += house_pos
        tmp.append(source)

        m = ManhattanMST()
        for t in tmp:
            m.add_point(t.y, t.x)
        u = UnionFind(n)
        x = 0
        index = 0
        tmp_house_joint_indices = [None] * (n - 1)
        for d, i, j in m.get_mst():
            x += d
            tmp_house_joint_indices[index] = [i, j]
            index += 1
        
        if x < cost:
            house_joint_indices = tmp_house_joint_indices[:]
            MST_min_source = source


    solver = Solver(N, source_pos, house_pos, C, P, house_joint_indices, MST_min_source)
    solver.solve()


if __name__ == "__main__":
    main()