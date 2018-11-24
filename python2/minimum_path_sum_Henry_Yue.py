class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Solve using dynamic programming
        if not grid or len(grid) == 0:
            return 0
        
        row_number = len(grid)
        column_number = len(grid[0])
        
        # Initialize result matrix with all 0s
        result_mat = [[0 for i in range(column_number)] for j in range(row_number)]
        
        # Initialize result matrix[0][0]
        result_mat[0][0] = grid[0][0]

        # Initialize result matrix first row
        for i in range(1, column_number):
            result_mat[0][i] = grid[0][i] + result_mat[0][i-1]

        # Initialize result matrix first column
        for j in range(1, row_number):
            result_mat[j][0] = grid[j][0] + result_mat[j-1][0]

        # Fill up the rest of the matrix
        for x in range(1, column_number):
            for y in range(1, row_number):
                if result_mat[y][x-1] < result_mat[y-1][x]:
                    result_mat[y][x] = result_mat[y][x-1] + grid[y][x]
                else:
                    result_mat[y][x] = result_mat[y-1][x] + grid[y][x]
        
        return result_mat[row_number-1][column_number-1]