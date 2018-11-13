public int[] twoSumGuangting(int[] nums, int target){
        if(nums == null || nums.length == 0) {
        return null;
        }

        int[] result = new int[2];
        HashMap<Integer, Integer> hm = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            if(hm.containsKey(target - nums[i])) {
                result[1] = i;
                result[0] = hm.get(target - nums[i]);
            } else {
                hm.put(nums[i], i);
        }

        return null;
        }
}