class Solution:
    def minimumDistance(self, nums):
        ans = float('inf')

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] == nums[j] == nums[k]:
                        distance = abs(i - j) + abs(j - k) + abs(k - i)
                        ans = min(ans, distance)

        return -1 if ans == float('inf') else ans
