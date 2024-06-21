class Solution:
    def equalFrequency(self, word: str) -> bool:
        if len(word) > 26:
            return False
        
        char_freq = {char: word.count(char) for char in word}
        #print(char_freq)

        freq_freq = {freq: list(char_freq.values()).count(freq) for freq in char_freq.values()}
        #print(freq_freq)

        if len(freq_freq) == 1:
            return True
        if len(freq_freq) > 2:
            return False
        if 1 in freq_freq.values():
            return True
        return False
    
tests = ["abcc", "aazz", "abccdd", "abc", "abbcc"]

S = Solution()

for test in tests:
    print(S.equalFrequency(test))