package java;

public class TwoSum {

    public static void main(String[] args){
        twoSum(new int[]{2, 7, 11, 15});
    }

    // time O(n^2)
    // space O(1)
    public static int[] twoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length; i++){
            for(int j = 0; j< nums.length; j++){
                if(i==j) continue;
                if(nums[i]+nums[j]==target){
                    return new int[]{i,j};
                }
            }
        }
        return new int[]{};
    }
}
