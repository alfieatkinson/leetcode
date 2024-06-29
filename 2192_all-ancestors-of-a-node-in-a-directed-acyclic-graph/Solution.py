from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        graph = defaultdict(list)
        in_degree = [0] * n

        print(graph, in_degree)

        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        print(graph, in_degree)

        topological_order = []
        queue = deque([node for node in range(n) if in_degree[node] == 0])

        print(topological_order, queue)

        while queue:
            node = queue.popleft()
            topological_order.append(node)

            for neighbour in graph[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        print(topological_order, queue)
            
        ancestors = [set() for _ in range(n)]

        print(ancestors)

        for node in topological_order:
            for neighbour in graph[node]:
                ancestors[neighbour].add(node)
                ancestors[neighbour].update(ancestors[node])

        print(ancestors)

        return [sorted(list(ancestor_set)) for ancestor_set in ancestors]

n = 8
edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]

S = Solution()

print(S.getAncestors(n, edges))