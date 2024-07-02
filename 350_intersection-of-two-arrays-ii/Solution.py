class Solution:
    def count(self, nums: list[int]) -> dict[int, int]:
        nums_count = {}
        for num in nums:
            if num in nums_count:
                nums_count[num] += 1
            else:
                nums_count[num] = 1
        return nums_count

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            nums_count = self.count(nums2)
            nums = nums1
        else:
            nums_count = self.count(nums1)
            nums = nums2

        print(nums_count)

        result = []
        for i in nums:
            if i in nums_count.keys():
                result.append(i)
                nums_count[i] -= 1
                if nums_count[i] == 0:
                    del nums_count[i]
        
        return result

S = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]

print(S.intersect(nums1, nums2))

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(S.intersect(nums1, nums2))

nums1 = [1,2,3,4]
nums2 = [3,5,4]

print(S.intersect(nums1, nums2))