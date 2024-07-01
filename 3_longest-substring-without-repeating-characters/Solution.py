class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""

        start = 0
        for i, char in enumerate(s):
            window = s[start:i+1]
            print(i, char)
            print(window)
            if char not in window[:-1]:
                if len(window) > len(substring):
                    substring = window
            else:
                while char in window[:-1]:
                    start += 1
                    window = s[start:i+1]
                    print(window)
        print(substring)
        return len(substring)

s = "abcabcbb"

solution = Solution()

print(solution.lengthOfLongestSubstring(s))