class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        total = 0

        for i, price in enumerate(cost):
            # Every 3rd candy can be free
            if i % 3 != 2:
                total += price

        return total