class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        total = m * n

        k %= total

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # Convert 2D index to 1D
                old_index = i * n + j

                # Shift right by k
                new_index = (old_index + k) % total

                # Convert 1D index back to 2D
                new_row = new_index // n
                new_col = new_index % n

                result[new_row][new_col] = grid[i][j]

        return result