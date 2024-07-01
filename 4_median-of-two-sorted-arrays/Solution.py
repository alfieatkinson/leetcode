class Solution:
    def mergeArrays(self, l1: list[int], l2: list[int]) -> list[int]:
        merged = []
        while l1 and l2:
            if l1[0] < l2[0]:
                merged.append(l1.pop(0))
            else:
                merged.append(l2.pop(0))
        merged += l1
        merged += l2
        return merged

    def findMedianSortedArrays(self, l1: list[int], l2: list[int]) -> float:
        merged = self.mergeArrays(l1, l2)
        n = len(merged)

        print(merged)

        if n % 2 == 0:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
        else:
            return merged[n // 2]

S = Solution()

l1 = [1, 2]
l2 = [3]

print(S.findMedianSortedArrays(l1, l2))

l1 = [1, 2]
l2 = [3, 4]

print(S.findMedianSortedArrays(l1, l2))