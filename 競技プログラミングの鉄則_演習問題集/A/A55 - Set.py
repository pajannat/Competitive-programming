# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
"""
ソート済み列をいくつかのバケット (list) に分割して管理します。このとき、(バケットの個数) : (バケット内の個数) くらいにします。(list の insert / pop の定数倍が軽く、バケット再構築の定数倍が重いため)
あるバケットが空になったり、多すぎたりしたら、1 度まとめて、均等にバケットに分割します。
基本的に、全ての操作が (要素数を  として)  時間で、(どのバケットか探す時間) < (バケットの中を探す時間) < (バケットへの挿入・削除) の順に重くなります。

SortedSet(a=[])
iterable から SortedSet を作ります。重複がなく、かつソートされていれば  時間、そうでなければ  時間です。

s.a
SortedSet の中身です。list の list になっていて、中には要素が昇順に並んでいます。各バケットには要素が存在することが保証されます。

len(s)
O(1) 時間

x in s / x not in s
O(√N) 時間

s.add(x)
x が s に含まれていなければ x を追加し、True を返します。償却 O(√N) 時間

s.discard(x)
x が s に含まれていれば x を削除し、True を返します。償却 O(√N) 時間

s.lt(x) / s.le(x) / s.gt(x) / s.ge(x)
x より小さい / 以下 / より大きい / 以上 で 最小 / 最大 の要素を返します。存在しなければ None を返します。O(√N) 時間

s[x]
下から x 番目 / 上から ~x 番目 の要素を返します。存在しない場合は IndexError を返します。O(√N) 時間

s.index(x)
x より小さい要素の数を返します。x が s に含まれている場合は list(s).index(x) に相当します。O(√N) 時間

s.index_right(x)
x 以下の要素の数を返します。O(√N) 時間
"""


import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
T = TypeVar('T')

class SortedSet(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
    
    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):
            a = sorted(set(a))
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
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
            if x <= a[-1]: return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
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
        if i != len(a) and a[i] == x: return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()
        return True

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x: return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0: self._build()
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
        if x < 0: x += self.size
        if x < 0: raise IndexError
        for a in self.a:
            if x < len(a): return a[x]
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
        return ans

def main():
    

    # 入力を受け取る
    Q = int(input())
    Query = []
    for _ in range(Q):
        Query.append(list(map(int, input().split())))
    
    s = SortedSet([])

    # 処理
    for q in Query:
        if q[0] == 1:
            s.add(q[1])
        elif q[0] == 2:
            s.discard(q[1])
        elif q[0] == 3:
            ans = s.ge(q[1])
            if ans == None:
                print(-1)
            else:
                print(ans)

 
if __name__ == "__main__":
    main()
