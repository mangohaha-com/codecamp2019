class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(grid)):
            max_xz = 0
            max_yz = 0
            for j in range(len(grid[i])):
                #xy
                if grid[i][j] > 0:
                    result += 1
                max_xz = max(max_xz, grid[i][j])
                max_yz = max(max_yz, grid[j][i])
            result += max_xz + max_yz
            
        return result