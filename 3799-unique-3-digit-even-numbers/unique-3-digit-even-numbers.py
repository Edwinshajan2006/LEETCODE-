from collections import Counter

class Solution:
    def totalNumbers(self, digits):
        count = Counter(digits)
        ans = 0

        for a in range(1, 10):       # Hundreds digit: cannot be 0
            for b in range(10):      # Tens digit
                for c in range(0, 10, 2):  # Units digit: must be even

                    # Check whether we have enough copies
                    needed = Counter([a, b, c])

                    if all(count[d] >= needed[d] for d in needed):
                        ans += 1

        return ans