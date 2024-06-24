class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        """
        @param nums (list[int]): a list of 0s and 1s.
        @param k (int): the number of bits in a row to flip at one time.
        @return flips (int): the minimum number of flips required to make all 1s.
        """
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

# Test examples
numss = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
]
ks = [1, 2, 3, 2, 2, 3, 3, 2, 2, 4]

S = Solution()
for i in range(0, len(numss)):
    print(f"Finding minimum flips of size {ks[i]} in the following list:\n{numss[i]}\n")
    result = S.minKBitFlips(numss[i], ks[i])
    if result < 0:
        print("Not possible.\n\n\n")
    else:
        print(f"Minimum number of flips: {result}.\n\n\n")