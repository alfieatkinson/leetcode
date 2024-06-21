class Solution:
    def myAtoi(self, s: str) -> int:
        if s == '':
            return 0

        s = s.strip()
        n = ''

        if s[0] == '-':
            n += '-'
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        for i in s:
            if i.isnumeric():
                if int(i) > 0:
                    n += i
            else:
                break
        
        if len(n) == 0 or n == '-':
            n = "0"

        if int(n) < -2**31: return -2**31
        elif int(n) > 2**31 - 1: return 2**31 - 1
        else: return int(n)
            
S = Solution()

tests = ["42", "   -42", "1337c0d3", "0-1", "words and 987", "-91283472332"]

for s in tests:
    print(S.myAtoi(s))