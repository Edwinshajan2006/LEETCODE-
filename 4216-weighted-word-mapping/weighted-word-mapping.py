class Solution:
    def mapWordWeights(self, words, weights):
        ans = ""

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            total %= 26

            ans += chr(ord('z') - total)

        return ans