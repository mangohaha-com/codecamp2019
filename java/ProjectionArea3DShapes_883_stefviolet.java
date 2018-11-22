class Solution {
    public int projectionArea(int[][] grid) {
        int n = grid.length;
        int x = 0;
        int z = 0;
        int y = 0;
        for (int i = 0; i < n; i++) {
            int mx = 0;
            int my = 0;
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 0) {
                    z++;
                }
                mx = Math.max(mx, grid[i][j]);
                my = Math.max(my, grid[j][i]);
            }
            x += mx;
            y += my;
        }
        return z + x + y;
    }
}
