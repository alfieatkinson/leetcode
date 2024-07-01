class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        n = len(arr)
        odds = list(map(lambda x: x % 2, arr))

        for i in range(n - 2):
            print(f"""
N: {i}
Arr: {arr[i]}
Odds: {odds[i]}
""")
            if odds[i] and odds[i + 1] and odds[i + 2]:
                print(arr[i:i + 3])
                return True
        return False
    
arr = [1,2,34,3,4,5,7,23,12]

S = Solution()

print(S.threeConsecutiveOdds(arr))