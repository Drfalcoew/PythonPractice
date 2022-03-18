class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        open_stack = []

        if len(s) % 2 == 1:
            return False

        min, max = 0, 0


        for i in range(len(s)):
            if locked[i] == '0':
                min -= 1
                max += 1
            elif s[i] == '(':
                min += 1
                max += 1
            else:
                min -= 1
                max -= 1

            if max < 0:
                return False
            if min < 0:
                min += 2

        return min == 0



mySolution = Solution().canBeValid("))()))", "010100")

print(mySolution)
