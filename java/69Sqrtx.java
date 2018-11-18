class Solution {
    public int mySqrt(int x) {
        if(x==0 || x == 1) return x;
        int left = 1;
        int right = x/2;
        while(left+1 < right) {
            int mid = left+(right-left)/2;
            System.out.println(mid);
            if(mid == x/mid) {
                return mid;   
            }else if(mid < x/mid) {
                left = mid;
            }else {
                right = mid-1;
            }
        }
        return right <= x/right ? right:left;
    }
}
