class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i



# TEST CASE 1 
# Input
# nums =
# [2,7,11,15]
# target =
# 9
# Output
# [0,1]
# Expected
# [0,1]

# TEST CASE 2
# Input
# nums =
# [3,2,4]
# target =
# 6
# Output
# [1,2]
# Expected
# [1,2]

# TEST CASE 3
# Input
# nums =
# [3,3]
# target =
# 6
# Output
# [0,1]
# Expected
# [0,1]
