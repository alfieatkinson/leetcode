class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        degrees = [0] * n

        for road in roads:
            degrees[road[0]] += 1
            degrees[road[1]] += 1

        print(degrees)

        sorted_cities = sorted(range(n), key=lambda x: degrees[x], reverse=True)

        print(sorted_cities)

        importances = [0] * n
        current_importance = n

        for city in sorted_cities:
            importances[city] = current_importance
            current_importance -= 1

        print(importances)

        total = 0
        for road in roads:
            total += importances[road[0]] + importances[road[1]]

        return total

roads = [[0,3],[2,4],[1,3]]

S = Solution()

print(S.maximumImportance(5, roads))