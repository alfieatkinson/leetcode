class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> bool:
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        alice = UnionFind(n + 1)
        bob = UnionFind(n + 1)

        used = 0
        removed = 0

        # Type 3 first
        for edge in edges:
            if edge[0] == 3:
                if alice.union(edge[1], edge[2]) | bob.union(edge[1], edge[2]):
                    used += 1
                else:
                    removed += 1

        # Alice edges
        for edge in edges:
            if edge[0] == 1:
                if alice.union(edge[1], edge[2]):
                    used += 1
                else:
                    removed += 1

        # Bob edges
        for edge in edges:
            if edge[0] == 2:
                if bob.union(edge[1], edge[2]):
                    used += 1
                else:
                    removed += 1

        # Check if both graphs are fully traversable
        if all(alice.find(i) == alice.find(1) for i in range(1, n + 1)) and \
           all(bob.find(i) == bob.find(1) for i in range(1, n + 1)):
            return removed
        else:
            return -1

n = 4
edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]

S = Solution()

print(S.maxNumEdgesToRemove(n, edges))