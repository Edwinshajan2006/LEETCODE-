class Solution:
    def minElement(self, nums):
        ans = float('inf')

        for num in nums:
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            ans = min(ans, total)

        return ans