class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for m in range(len(grid)):
            for n in range(len(grid[m])):
                if m == 0 and n == 0:
                    continue
                if m == 0 and n != 0:
                    grid[m][n] += grid[m][n-1]
                elif m != 0 and n == 0:
                    grid[m][n] += grid[m-1][n]
                else:
                    grid[m][n] += min(grid[m-1][n], grid[m][n-1])
        return grid[m][n]