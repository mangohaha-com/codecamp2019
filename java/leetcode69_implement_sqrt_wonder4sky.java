public leetcode69_implement_sqrt_wonder4sky{

// 方法一： binary search
class Solution {
    public int mySqrt(int x) {
        // 复习binary search的写法！！！！
        // 时间复杂度：log(n)!!!!!
        // 如果遇上需要扫一遍找到数来找到某个数时，记得二分法！！1
        // 要敏感，x是一个从零到最大integer的数，二分法！！
        if (x == 0) return 0;
        int start = 1;
        int end = x;
        // int mid; 要写在循环里面

        // 循环的条件是 while (start < end)
        while (start < end) {
            int mid = (start + end) / 2;

            if (mid <= x / mid && (mid + 1) > x / (mid + 1))
                return mid;
            else if (mid > x / mid)
                end = mid;
            else
                start = mid;
        }
        return start;  // 为什么最后要return start？！！！

    }
}

// 方法二： newton 算法 （best）
class Solution {
    public int mySqrt(int x) {
        // newton solution; O(lg(x))
        // 不懂这个方法， 问！
        if (x == 0) return 0;
        long i = x;
        while (i > x / i)
            i = (i + x / i) / 2;
        return (int) i;

    }
}

// 方法三：暴力
class Solution {
    public int mySqrt(int x) {

        // 运行时间太长，not a good 算法

        for (int i = 0; ; i++) {

            // 不能写成if (i * i <= x && (i + 1) * (i + 1) < x), 因为这样可能会造成越界
            // 防止越界的逆向思维：如果i＊i > x, 那么x /i 应该小于i （这样就可以防止越界）
            if (i * i <= x && x / (i + 1) < (i + 1)) {
                return i;
            } else if ((i * i < x) && ((i + 1) * (i + 1) == x))
                return i + 1;
        }
    }
}

}

