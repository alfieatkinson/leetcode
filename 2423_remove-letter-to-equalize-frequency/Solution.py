from statistics import mode

class Solution:
    def equalFrequency(self, word: str) -> bool:
        if len(word) > 26:
            return False
        
        char_freq = {char: word.count(char) for char in word}
        print(char_freq)

        freqs = list(char_freq.values())
        print(freqs)

        #freq_freq = {freq: list(char_freq.values()).count(freq) for freq in char_freq.values()}
        #print(freq_freq)

        m = mode(freqs)
        print(mode)



        return False
    
tests = ["abcc", "aazz", "abccdd", "abc", "abbcc", "cbccca"]

S = Solution()

for test in tests:
    print(S.equalFrequency(test))