#!/usr/bin/env python3
# -*- coding:utf-8 -*-
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #dp to solve problem
        r=len(grid)
        c=len(grid[0])
        #Initialize first column of total cost array
        for i in range(1,c):
            grid[0][i]+=grid[0][i-1]
        #Initialize first row of total cost array
        for j in range(1,r):
            grid[j][0]+=grid[j-1][0]
        #construct rest of array
        for i in range(1,r):
            for j in range(1,c):
                grid[i][j]+=min( grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]
