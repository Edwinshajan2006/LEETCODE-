class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Get unique values in sorted order
        sorted_unique = sorted(set(arr))

        # Map each value to its rank
        rank = {value: i + 1 for i, value in enumerate(sorted_unique)}

        # Replace each element with its rank
        return [rank[x] for x in arr]