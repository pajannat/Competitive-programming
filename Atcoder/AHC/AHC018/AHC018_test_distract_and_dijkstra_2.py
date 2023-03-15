from enum import Enum
from typing import List
import sys

import random


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

    # def __init__(self, N: int, source_pos: List[Pos], house_pos: List[Pos], C: int, P: int, house_joint_indices: List, MST_min_source: Pos, test_destruct: List[Pos]):
    def __init__(self, N: int, source_pos: List[Pos], house_pos: List[Pos], C: int, P: int):
        self.N = N
        self.source_pos = source_pos
        self.source_pos_org = source_pos[:]
        self.house_pos = house_pos
        self.house_pos_org = house_pos[:]
        self.C = C
        self.P = P
        self.field = Field(N, C)
        self.field_org = Field(N, C)


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

    # def test_destruction(self):
    #     for test_dest in self.test_destruct:
    #         y, x = test_dest.y, test_dest.x
    #         res = self.destruct_test(y, x)
    #         if res == Response.BROKEN:
    #             self.house_pos.append(Pos(y, x))
    #     self.house_pos_org = self.house_pos[:]

    def test_destruction_hoge(self, test_destruct, power):
        BROKEN_pos = []
        for test_dest in test_destruct:
            y, x = test_dest.y, test_dest.x
            res = self.destruct_test(y, x, power)
            if res == Response.BROKEN:
                BROKEN_pos.append(Pos(y, x))
        return BROKEN_pos

    def solve(self):
        # # 何か所か試し掘りする
        # self.test_destruction()

        # self.house_joint_indices, self.MST_min_sourceを計算
        self.house_joint_indices, self.MST_min_source = find_MST_min_source(self.source_pos, self.house_pos)

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
        source_pos = self.source_pos_org[:]
        house_pos = self.house_pos_org[:]
        for test_dest in self.test_destruct:
            y, x = test_dest.y, test_dest.x
            cnt = self.destruct(y, x)
            if cnt <= 1:
                house_pos = [Pos(y, x)] + house_pos[:]

        # それぞれの houceから, 最も近い水源へ進む
        for house in house_pos:
            source = min_Manhattan_dist_source(house, source_pos)
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


    def destruct_test(self, y: int, x: int, p: int):
        # excavate (y, x) with fixed power until destruction
        power = p

        if not self.field.is_broken[y][x]:
            result = self.field.query(y, x, power)
            if result == Response.FINISH:
                print(f"total_cost={self.field.total_cost}", file=sys.stderr)
                sys.exit(0)
            elif result == Response.INVALID:
                print(f"invalid: y={y} x={x}", file=sys.stderr)
                sys.exit(1)
            elif result == Response.BROKEN:
                return result
            elif result == Response.NOT_BROKEN:
                return result


def Manhattan_dist(y1, x1, y2, x2):
    z1 = x1 + y1
    z2 = x2 + y2
    w1 = x1 - y1
    w2 = x2 - y2
    # dist = max(abs(z1 - z2), abs(w1 - w2))
    dist = abs(y2-y1) + abs(x2-x1)
    return dist

def min_Manhattan_dist_source(house_pos_i, source_pos):
    min_dist = 100000 # N=200 より, マンハッタン距離は400以下
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

def find_MST_min_source(source_pos, house_pos):
    n = len(house_pos) + 1
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
    return house_joint_indices, MST_min_source

def dijkstra(matrix_list, start, terminal):
 
    import math
 
    route_list = matrix_list # 初期のノード間の距離のリスト
 
    isolate_num = 0
    isolated_list = []
    node_num = len(route_list) #ノードの数
    unsearched_nodes = list(range(node_num)) # 未探索ノード
    distance = [math.inf] * node_num # ノードごとの距離のリスト
    previous_nodes = [-1] * node_num # 最短経路でそのノードのひとつ前に到達するノードのリスト
    distance[start] = 0 # 初期のノードの距離は0とする
 
    for isolate in unsearched_nodes:#孤立したノードを探索済にする
        if route_list[isolate].count(0) == node_num:
            unsearched_nodes.remove(isolate)
            distance[isolate] = -isolate
 
    while(len(unsearched_nodes) != 0): #未探索ノードがなくなるまで繰り返す
        possible_min_distance = math.inf # 最小のdistanceを見つけるための一時的なdistance。初期値は inf に設定。
         # まず未探索ノードのうちdistanceが最小のものを選択する
        min = math.inf
        target_min_index = unsearched_nodes[0] # target_min_index の初期化
        for target in unsearched_nodes:
            if distance[target] < min:
                min = distance[target]
                target_min_index = target
                # print(f"min={min}, target_min_index={target_min_index}", file=sys.stderr)
        # print(f"unsearched_nodes={unsearched_nodes}, target_min_index={target_min_index}", file=sys.stderr)
        unsearched_nodes.remove(target_min_index) # 探索するので未探索リストから除去
        target_edge = route_list[target_min_index] # ターゲットになるノードからのびるエッジのリスト
        for index, route_dis in enumerate(target_edge):
            if route_dis != 0:
                if distance[index] > (distance[target_min_index] + route_dis):
                    distance[index] = distance[target_min_index] + route_dis # 過去に設定されたdistanceよりも小さい場合はdistanceを更新
                    if index != start:
                        previous_nodes[index] =  target_min_index #　ひとつ前に到達するノードのリストも更新
 
    # 経路を格納
    previous_node = terminal
    path = []
    while previous_node != -1:
        path.append(previous_node)
        previous_node = previous_nodes[previous_node]
    path.reverse()
 
    return distance[terminal], path


# def pos2Gidx(pos, grid_num, grid_interval):
#     Gidx = grid_num * (pos.y//grid_interval) + 1 * (pos.x//grid_interval)
#     return Gidx
def pos2Gidx(pos, grid_start_y, grid_start_x, grid_num_y, grid_num_x, grid_interval_y, grid_interval_x):
    Gidx = grid_num_x * ((pos.y-grid_start_y)//grid_interval_y) + 1 * ((pos.x-grid_start_x)//grid_interval_x)
    return Gidx

# def Gidx2pos(Gidx, grid_num, grid_interval):
#     tmp_y = (Gidx // grid_num) * grid_interval
#     tmp_x = (Gidx % grid_num) * grid_interval
#     tmp_pos = Pos(tmp_y, tmp_x)
#     return tmp_pos

def Gidx2pos(Gidx, grid_start_y, grid_start_x, grid_num_y, grid_num_x, grid_interval_y, grid_interval_x):
    tmp_y = grid_start_y + (Gidx // grid_num_x) * grid_interval_y
    tmp_x = grid_start_x + (Gidx % grid_num_x) * grid_interval_x
    tmp_pos = Pos(tmp_y, tmp_x)
    return tmp_pos


def chk_adj_list(adj_list):
    flg = True
    # タテヨコの数チェック
    W = len(adj_list[0])
    for i in range(len(adj_list)):
        if len(adj_list[i]) != W:
            print(f"隣接リストタテヨコの数おかしい!!!", file=sys.stderr)
            return

    # 対称性チェック
    for i in range(len(adj_list)):
        for j in range(len(adj_list[0])):
            if adj_list[i][j] == adj_list[j][i]:
                pass
            else:
                flg = False

    if flg:
        print(f"隣接リスト大丈夫!!!", file=sys.stderr)
    elif not flg:
        print(f"隣接リスト対称性おかしい!!!", file=sys.stderr)



def main():
    N, W, K, C = [int(v) for v in input().split(" ")]
    source_pos = []
    house_pos = []

    grid_num = 20
    grid_interval = N // grid_num
    grid_start_y = 8
    grid_start_x = 8
    grid_interval_y = 8
    grid_interval_x = 8
    grid_num_y = 1 + ((N-grid_start_y) // grid_interval_y)
    grid_num_x = 1 + ((N-grid_start_x) // grid_interval_x)

    test_destruct_grid = []
    # test_destruct_grid_broken = [[0] * grid_num for _ in range(grid_num)]
    test_destruct_grid_broken = [[0] * grid_num_x for _ in range(grid_num_y)]


    # グリッド上の試し掘りする点を指定(リストとして用意)
    for y in range(grid_start_y, N, grid_interval_y):
        for x in range(grid_start_x, N, grid_interval_x):
            test_destruct_grid.append(Pos(y, x))

    # # グリッド上の試し掘りする点を指定(リストとして用意)
    # for y in range(grid_interval, N, grid_interval):
    #     for x in range(grid_interval, N, grid_interval):
    #         test_destruct_grid.append(Pos(y, x))


    for _ in range(W):
        y, x = (int(v) for v in input().split(" "))
        source_pos.append(Pos(y, x))
    for _ in range(K):
        y, x = (int(v) for v in input().split(" "))
        house_pos.append(Pos(y, x))

    
    # power を決定する
    P = 100

    # 処理

    # Solver インスタンス生成
    solver = Solver(N, source_pos, house_pos, C, P)

    # 試し掘り実行
    from collections import defaultdict
    broken_pos = []
    broken_pos_and_cost = defaultdict(lambda: 0)

    test_P1 = 64
    # 1週目の試し掘り
    tmp_broken_pos = solver.test_destruction_hoge(test_destruct_grid, test_P1)
    broken_pos += tmp_broken_pos
    for tmp_pos in tmp_broken_pos:
        broken_pos_and_cost[str(tmp_pos.y) + "," + str(tmp_pos.x)] += test_P1
    # broken_pos = solver.test_destruction_hoge(test_destruct_grid, test_P1)
    
    # test_P2 = test_P1*4
    # # 2週目の試し掘り
    # tmp_broken_pos = solver.test_destruction_hoge(test_destruct_grid, test_P2)
    # broken_pos += tmp_broken_pos
    # for tmp_pos in tmp_broken_pos:
    #     broken_pos_and_cost[str(tmp_pos.y) + "," + str(tmp_pos.x)] += (test_P1 + test_P2)

    # test_P3 = test_P1*4
    # # 3週目の試し掘り
    # tmp_broken_pos = solver.test_destruction_hoge(test_destruct_grid, test_P3)
    # broken_pos += tmp_broken_pos
    # for tmp_pos in tmp_broken_pos:
    #     broken_pos_and_cost[str(tmp_pos.y) + "," + str(tmp_pos.x)] += (test_P1 + test_P2 + test_P3)

    print(f"broken_pos_len={len(broken_pos)}", file=sys.stderr)

    # デバッグのため print
    # print(f"inpupt={N, W, K, C}", file=sys.stderr)
    for pos in broken_pos:
        print(f"pos={pos.y, pos.x, grid_interval, len(test_destruct_grid_broken)}", file=sys.stderr)
        # test_destruct_grid_broken[pos.y // grid_interval][pos.x // grid_interval] = 1
        test_destruct_grid_broken[(pos.y-grid_start_y) // grid_interval_y][(pos.x-grid_start_x) // grid_interval_x] = 1
    # print(f"test_destruct_grid_broken={test_destruct_grid_broken}", file=sys.stderr)

    # print(f"broken_pos_and_cost={broken_pos_and_cost}", file=sys.stderr)


    # 隣接リストの作成（重み付きグラフなので、各辺について (隣接頂点, 重み) のタプルを記録する）
    # G = [ [0]*(grid_num**2) for i in range(grid_num**2) ]
    G = [ [0]*(grid_num_y*grid_num_x) for i in range(grid_num_y*grid_num_x) ]
    for pos1 in test_destruct_grid:
        for pos2 in test_destruct_grid:
                # pos1 == pos2 はスキップ
                if (pos1.y == pos2.y) and (pos1.x == pos2.x):
                    continue
                # pos1, pos2 がグリッド上で隣接していない場合はスキップ
                if abs(pos1.y - pos2.y) + abs(pos1.x - pos2.x) > grid_interval:
                    continue

                # # pos1, pos2 がグリッド上で隣接していない場合はスキップ
                # if abs(pos1.y - pos2.y) > grid_interval_y:
                #     continue
                # if abs(pos1.x - pos2.x) > grid_interval_x:
                #     continue


                # pos1, pos2 の岩盤が破壊済みか否か
                pos1_broken_flg = False
                pos2_broken_flg = False
                # if test_destruct_grid_broken[pos1.y//grid_interval][pos1.x//grid_interval]:
                #     pos1_broken_flg = True
                # if test_destruct_grid_broken[pos2.y//grid_interval][pos2.x//grid_interval]:
                #     pos2_broken_flg = True
                if test_destruct_grid_broken[(pos1.y-grid_start_y) // grid_interval_y][(pos1.x-grid_start_x) // grid_interval_x]:
                    pos1_broken_flg = True
                if test_destruct_grid_broken[(pos2.y-grid_start_y) // grid_interval_y][(pos2.x-grid_start_x) // grid_interval_x]:
                    pos2_broken_flg = True
                
                # 隣接リストに値を設定
                # a = pos2Gidx(pos1, grid_num, grid_interval)
                # b = pos2Gidx(pos2, grid_num, grid_interval)
                a = pos2Gidx(pos1, grid_start_y, grid_start_x, grid_num_y, grid_num_x, grid_interval_y, grid_interval_x)
                b = pos2Gidx(pos2, grid_start_y, grid_start_x, grid_num_y, grid_num_x, grid_interval_y, grid_interval_x)

                # if broken_pos_and_cost[b] == 0:
                #     G[a][b] = 50000
                # else:
                #     G[a][b] = broken_pos_and_cost[b]

                # if broken_pos_and_cost[a] == 0:
                #     G[a][b] = 50000
                # else:                
                #     G[b][a] = broken_pos_and_cost[a]

                # pos1, pos2 どちらの岩盤も破壊済みの場合
                if pos1_broken_flg and pos2_broken_flg:
                    c = 1 * 10 # 採掘回数の目安
                    G[a][b] = broken_pos_and_cost[str(pos2.y) + "," + str(pos2.x)]
                    G[b][a] = broken_pos_and_cost[str(pos1.y) + "," + str(pos1.x)]
                    # print(f"broken_pos_and_cost[a]={broken_pos_and_cost[a]}", file=sys.stderr)
                    # G[a][b] = c
                    # G[b][a] = c
                # pos1, pos2 のどちらかの岩盤のみ破壊済み
                elif (pos1_broken_flg and not pos2_broken_flg) or (not pos1_broken_flg and pos2_broken_flg):
                    c = ((500000 // P) * 10) // 2
                    G[a][b] = c
                    G[b][a] = c
                # pos1, pos2 どちらの岩盤も破壊されていない場合
                elif (not pos1_broken_flg) and (not pos2_broken_flg):
                    c = (500000 // P) * 10
                    G[a][b] = c
                    G[b][a] = c


    # それぞれの家と最近傍の broken_pos をつなげる
    house_broken_pos = [] # それぞれの家と最近傍の broken_pos のリスト
    for start_pos in house_pos:
        goal_pos = min_Manhattan_dist_source(start_pos, broken_pos)
        house_broken_pos.append([start_pos, goal_pos])
    # for s_pos, g_pos  in house_broken_pos:
    #     print(f"s_pos={s_pos.y, s_pos.x}, g_pos={g_pos.y, g_pos.x}", file=sys.stderr)


    source_broken_pos = [] # それぞれの水源と最近傍の broken_pos のリスト
    for start_pos in source_pos:
        goal_pos = min_Manhattan_dist_source(start_pos, broken_pos)
        source_broken_pos.append([start_pos, goal_pos])
    # for s_pos, g_pos in source_broken_pos:
    #     print(f"s_pos={s_pos.y, s_pos.x}, g_pos={g_pos.y, g_pos.x}", file=sys.stderr)


    # broken_pos(家と連結) から すべての broken_pos(水源と連結) へダイクストラ
    # 経路が最短のものを採用
    for house_broken_pos_i in house_broken_pos:
        # broken_pos(家と連結)
        h_broken_pos = house_broken_pos_i[1]
        now_dist = math.inf
        now_path = []
        for source_broken_pos_i in source_broken_pos:
            # broken_pos(水源と連結)
            s_broken_pos = source_broken_pos_i[1]

            # h_broken_pos, s_broken_pos でダイクストラ
            # 経路長と経路を記録
            # tmp_dist, tmp_path = dijkstra(G, pos2Gidx(h_broken_pos, grid_num, grid_interval), pos2Gidx(s_broken_pos, grid_num, grid_interval))
            tmp_dist, tmp_path = dijkstra(G, pos2Gidx(h_broken_pos, grid_start_y, grid_start_x, grid_num_y, grid_num_x, grid_interval_y, grid_interval_x), pos2Gidx(s_broken_pos, grid_start_y, grid_start_x, grid_num_y, grid_num_x, grid_interval_y, grid_interval_x))
            # 経路長が最短のものを採用
            if tmp_dist < now_dist:
                now_path = tmp_path
                now_dist = tmp_dist
        print(f"h_broken_pos={h_broken_pos.y, h_broken_pos.x}, s_broken_pos={s_broken_pos.y, s_broken_pos.x}", file=sys.stderr)
        print(f"now_dist={now_dist}, now_path={now_path}", file=sys.stderr)
        print(f"", file=sys.stderr)

        # broken_pos(家と連結) から broken_pos(水源と連結) の最短経路を掘る
        s_pos = h_broken_pos
        g_pos = h_broken_pos
        for goal_idx in now_path:
            # g_pos = Gidx2pos(goal_idx, grid_num, grid_interval)
            g_pos = Gidx2pos(goal_idx, grid_start_y, grid_start_x, grid_num_y, grid_num_x, grid_interval_y, grid_interval_x)
            print(f"s={s_pos.y, s_pos.x}, g={g_pos.y, g_pos.x}", file=sys.stderr)
            solver.move(s_pos, g_pos)
            s_pos = g_pos


    # それぞれの家と最近傍の broken_pos をつなげる
    for house_broken_pos_i in house_broken_pos:
        print(f"s={house_broken_pos_i[0].y, house_broken_pos_i[0].x}, g={house_broken_pos_i[1].y, house_broken_pos_i[1].x}", file=sys.stderr)
        solver.move(house_broken_pos_i[0], house_broken_pos_i[1])

    # それぞれの水源と最近傍の broken_pos をつなげる
    for source_broken_pos_i in source_broken_pos:
        solver.move(source_broken_pos_i[0], source_broken_pos_i[1])

    # for pos in broken_pos:
    #     print(f"test_BROKEN_pos={pos.y, pos.x}", file=sys.stderr)
    
    # for g in G:
    #     print(f"g={g}", file=sys.stderr)


    # solve()
    # solver.solve()


if __name__ == "__main__":
    main()