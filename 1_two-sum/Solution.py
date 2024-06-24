class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        @param nums (list[int]): a list of integers.
        @param target (int): the target sum.
        @return indices (list[int]): the indices of the two numbers that sum to target.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
S = Solution()

tests = [
    [2, 7, 11, 15],
    [3, 2, 4],
    [3, 3]
]

targets = [9, 6, 6]

for i in range(0, len(tests)):
    print(S.twoSum(tests[i], targets[i]))