class Solution {
    public int mySqrt(int x) {
        if (x <= 1) {
            return x;
        }
        int start = 1;
        int end = x;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (mid == x / mid) {
                return mid;
            }
            if (mid < x / mid) {
                start = mid;
            } else {
                end = mid - 1;
            }
        }
        if (end <= x / end) {
            return end;
        }
        return start;
    }
}
