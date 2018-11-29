public class leetcode561_array_partition_1_wonder4sky {

    class Solution {
        public int arrayPairSum(int[] nums) {
            // 这道题是求as large as possible;
            // 方法一：所以把数组排好序，两两比较，把最小的拿出来相加即可 时间复杂O(nlgn)
            // 不需要first, second变量
            // 方法二：用hash function做，时间复杂度O(n),但还没想明白
            // 如果是求as small as possible; 就不需要两两比较，而是可以直接拿出数组的前一半相加即可
            /**
             * 有一些methods是static void， 所以不需要一个具体的object.method,
             * 而是该method所在的class.method, e.g.: Arrays.sort(nums); Math.min(a,b).
             **/

            int sum = 0;

            Arrays.sort(nums);

            int n = nums.length;
            // int first = 0;
            // int second = 1;

            for (int i = 0; i < n; i+=2) {
                sum += nums[i];
                // first += 2; // 注意指针是走两步，而不是走一步
                // second += 2;
            }
            return sum;
        }
    }
}
