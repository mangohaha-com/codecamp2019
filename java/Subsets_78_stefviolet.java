class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        helper(res, new ArrayList<>(), nums, 0);
        return res;
    }
    private void helper(List<List<Integer>> res, List<Integer> list, int[] nums, int curr) {
        res.add(new ArrayList<Integer>(list));
        for (int i = curr; i < nums.length; i++) {
            list.add(nums[i]);
            helper(res, list, nums, i + 1);
            list.remove(list.size() - 1);
        }
    }
}
