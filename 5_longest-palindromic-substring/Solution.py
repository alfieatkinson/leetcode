class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) % 2 == 0:
            s = ''.join('#' + c for c in s) + '#'
        
        n = len(s)
        s = '$' + s + '^'
        lengths = [0] * (n + 2)
        left, right = 1, 1
        for centre in range(1, n + 1):
            mirror = left + (right - centre)
            lengths[centre] = max(0, min(right - centre, lengths[mirror]))
            while s[centre + 1 + lengths[centre]] == s[centre - 1 - lengths[centre]]:
                lengths[centre] += 1
            if centre + lengths[centre] > right:
                left, right = centre - lengths[centre], centre + lengths[centre]
        
        print(f"""
String: {s[1:-1]}
Lengths: {lengths[1:-1]}
""")

S = Solution()

s = "babad"

print("ANSWER:", S.longestPalindrome(s))

s = "cbbd"

print("ANSWER:", S.longestPalindrome(s))