class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid==None or grid==[]:
            return None
        n=len(grid[0])
        m=len(grid)
        
        dp=[0 for _ in range (n)]
        dp[0]=grid[0][0]
        
        for i in range (1,n):
            dp[i]=dp[i-1]+grid[0][i]
        
        for i in range (1,m):
            dp[0]+=grid[i][0]
            for j in range (1,n):
                if dp[j-1]<dp[j]:
                    dp[j]=dp[j-1]+grid[i][j]
                else:
                    dp[j]=dp[j]+grid[i][j]
        
        return dp[-1] if dp else 0
            
