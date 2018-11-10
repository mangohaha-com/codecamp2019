## 463 Island Perimeter



```java

class Solution {
    public int islandPerimeter(int[][] grid) {
        if(grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        int[][] neighbor = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        Set<Integer> set = new HashSet<>();
        int m = grid.length;
        int n = grid[0].length;
        
        int res = 0;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 1) {
                    res+=4;
                    
                    set.add(i*n+j);
                    for(int[] nei: neighbor) {
                        
                        if((nei[0]+i) >= 0 &&  (nei[0]+i) < m &&
                           (nei[1]+j) >= 0 && (nei[1]+j) < n && set.contains((nei[0]+i)*n+j+nei[1])) {
                            res-=2;
                        }
                    }
                }else {
                    
                }
            }
        }
        return res;
    }
}
```

