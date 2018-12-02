public class Solution {
    public int mySqrt(int x) {
        long i = 0;
        long j = x / 2 + 1;
        while (i <= j) {
            long mid = (i + j) / 2;
            if (mid * mid == x)
                return (int)mid;
            if (mid * mid < x)
                i = mid + 1;
            else
                j = mid - 1;
        }
        return (int)j;
    }
}
