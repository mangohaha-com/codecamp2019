class Solution {
    public int reverse(int x) {
        int result = 0;
        while (x != 0) {
            int temp = 10 * result + x % 10;
            // Test for overflow
            if (temp / 10 != result) {
                return 0;
            }
            result = temp;
            x /= 10;
        }
        return result;
    }
}
