class Solution {
    private int[][] mem;
    public int minPathSum(int[][] grids) {
        int m = grids.length, n = grids[0].length;
        mem = new int[m][n];
        return gridSum(grids, m - 1 , n - 1);

    }
    
    private int gridSum(int[][] grids, int m, int n) {
        if (m == 0 && n == 0) return grids[0][0];
        if (mem[m][n] != 0) return mem[m][n];
        if (m == 0) {
            mem[0][n] = grids[0][n] + gridSum(grids,0, n - 1);
            return mem[0][n];
        }
        if (n == 0){
            mem[m][0] = grids[m][0] + gridSum(grids,m - 1, 0);
            return mem[m][0];
        }
        mem[m][n] = grids[m][n] + Math.min(gridSum(grids,m - 1, n), gridSum(grids, m, n - 1));
        return mem[m][n];
    }
}