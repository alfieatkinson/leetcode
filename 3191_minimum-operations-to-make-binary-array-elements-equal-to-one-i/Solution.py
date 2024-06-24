class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        @param nums (list[int]): a list of 0s and 1s.
        @return flips (int): the minimum number of flips required to make all 1s.
        """
        k = 3
        n = len(nums)
        flips = 0
        flipped = [0] * n
        flip_count = 0

        for i in range(n):
            if i >= k:
                flip_count -= flipped[i - k]
            
            if (nums[i] + flip_count) % 2 == 0:
                if i + k > n:
                    print(f"Flips: {flips}\nFlipped: {flipped}\nFlip Count: {flip_count}\n")
                    return -1
                flips += 1
                flip_count += 1
                flipped[i] = 1

            print(f"Flips: {flips}\nFlipped: {flipped}\nFlip Count: {flip_count}\n")
        
        return flips