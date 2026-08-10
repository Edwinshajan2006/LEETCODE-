from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest = min(nums)
        largest = max(nums)

        nums_set = set(nums)
        missing = []

        for i in range(smallest, largest + 1):
            if i not in nums_set:
                missing.append(i)

        return missing