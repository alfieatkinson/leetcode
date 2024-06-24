class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        @param nums (list[int]): a list of integers.
        @param target (int): the target sum.
        @return indices (list[int]): the indices of the two numbers that sum to target.
        """
        n = len(nums)
        hashmap = {}

        # Create a hashmap from the nums list elements and their indices.
        for i in range(n):
            hashmap[nums[i]] = i

        # Iterate through the nums list and check if the complement needed to get to target is in the hashmap.
        for i in range(n):
            x = target - nums[i]
            if x in hashmap and hashmap[x]!= i:
                return [i, hashmap[x]]
                
S = Solution()

tests = [
    [2, 7, 11, 15],
    [3, 2, 4],
    [3, 3]
]

targets = [9, 6, 6]

for i in range(0, len(tests)):
    print(S.twoSum(tests[i], targets[i]))