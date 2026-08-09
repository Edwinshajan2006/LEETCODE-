class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)

        pushes = 0

        for i in range(n):
            cost = i // 8 + 1
            pushes += cost

        return pushes