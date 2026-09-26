class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            reverse_pos = 26 - (ord(s[i]) - ord('a'))
            position = i + 1
            total += reverse_pos * position

        return total