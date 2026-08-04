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



# # TEST CASES 
# Accepted
# Runtime: 0 ms
# Case 1
# Case 2
# Case 3
# Input
# nums =
# [1,4,2,5]
# Output
# [3]
# Expected
# [3]

# Accepted
# Runtime: 0 ms
# Case 1
# Case 2
# Case 3
# Input
# nums =
# [7,8,6,9]
# Output
# []
# Expected
# []


# Accepted
# Runtime: 0 ms
# Case 1
# Case 2
# Case 3
# Input
# nums =
# [5,1]
# Output
# [2,3,4]
# Expected
# [2,3,4]
