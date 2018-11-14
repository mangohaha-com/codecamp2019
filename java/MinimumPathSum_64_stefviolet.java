class Solution {
    public int minPathSum(int[][] grid) {
        // DP
        int[] path = new int[grid[0].length];
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (i == 0) {
                    path[j] = grid[i][j] + (j == 0 ? 0 : path[j - 1]);
                } else {
                    path[j] = (j == 0 ? path[j] : Math.min(path[j], path[j - 1])) + grid[i][j];
                }
            }
        }
        return path[path.length - 1];
    }
}
