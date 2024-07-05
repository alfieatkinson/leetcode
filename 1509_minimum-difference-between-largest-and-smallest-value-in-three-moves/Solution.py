class Solution:
    def partition(self, nums: list[int], low: int, high: int) -> list[int]:
        pivot = nums[low]
        start = low + 1
        end = high

        while True:
            while start <= end and nums[end] >= pivot:
                end = end - 1
            while start <= end and nums[start] <= pivot:
                start = start + 1
            
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
            else:
                break

        nums[low], nums[end] = nums[end], nums[low]

        return end

    def quickSort(self, nums: list[int], start: int, end: int) -> list[int]:
        if start < end:
            partition_index = self.partition(nums, start, end)

            self.quickSort(nums, start, partition_index - 1)
            self.quickSort(nums, partition_index + 1, end)

    def minDifference(self, nums: list[int], swaps: int = 3) -> int:
        if len(nums) <= 4:
            return 0
        
        print(nums)
        self.quickSort(nums, 0, len(nums) - 1)
        print(nums)
        
        n = len(nums)
        if swaps >= n - 1:
            return 0
        
        min_diff = float('inf')
        for i in range(swaps + 1):
            current_diff = nums[n - 1 - (swaps - i)] - nums[i]
            min_diff = min(min_diff, current_diff)

        return min_diff

S = Solution()

nums = [5,3,2,4]

print(S.minDifference(nums))

nums = [1,5,0,10,14]

print(S.minDifference(nums))

nums = [3,100,20]

print(S.minDifference(nums))