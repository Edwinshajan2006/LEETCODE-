class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        if len({x % 2 for x in nums1}) == 1:
            return True

        return len(nums1) > 1