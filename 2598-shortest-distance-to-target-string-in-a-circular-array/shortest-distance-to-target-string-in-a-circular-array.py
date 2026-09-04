from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = float('inf')

        for i in range(n):
            if words[i] == target:
                direct = abs(i - startIndex)
                circular = n - direct
                ans = min(ans, direct, circular)

        return -1 if ans == float('inf') else ans