class Solution:
    def findMissingElements(self, nums):
        minimum = min(nums)
        maximum = max(nums)

        result = []

        for i in range(minimum, maximum + 1):
            if i not in nums:
                result.append(i)

        return result