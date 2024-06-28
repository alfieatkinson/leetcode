class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        connections = [[] for i in range(n)]

        for road in roads:
            connections[road[0]].append(road[1])
            connections[road[1]].append(road[0])

        print(connections)

        connections_sorted = sorted(connections, key=len, reverse=True)

        print(connections_sorted)

        importances = [n - connections_sorted.index(i) for i in connections]

        print(importances)

roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]

S = Solution()

print(S.maximumImportance(5, roads))