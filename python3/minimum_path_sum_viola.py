"""
week 3

code has passed on leetcode.com
"""
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        w_grid = [[ 999 for i in range(len(grid[0])+1)] for i in range(len(grid)+1)]
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                if j < len(grid[0]) - 1 and i < len(grid) - 1:
                    if w_grid[i+1][j] <= w_grid[i][j+1]:
                        w_grid[i][j] = w_grid[i+1][j] + grid[i][j]
                    else:
                        w_grid[i][j] = w_grid[i][j+1] + grid[i][j]
                elif j == len(grid[0]) - 1 and i == len(grid) - 1:
                    w_grid[i][j] = grid[i][j]
                elif j == len(grid[0]) - 1:
                    w_grid[i][j] = w_grid[i+1][j] + grid[i][j]
                elif i == len(grid) - 1:
                    w_grid[i][j] = w_grid[i][j+1] + grid[i][j]
                else:
                    continue

        p_x, p_y = 0, 0
        rst = grid[0][0]
        for _ in range(len(grid) + len(grid[0]) - 2):
            if w_grid[p_x + 1][p_y] <= w_grid[p_x][p_y + 1]:
                rst += grid[p_x + 1][p_y]
                p_x += 1
            else:
                rst += grid[p_x][p_y + 1]
                p_y += 1

        return rst
