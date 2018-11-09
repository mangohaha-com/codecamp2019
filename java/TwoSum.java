package java;

import java.util.HashMap;
import java.util.Map;

import org.junit.Assert;
import org.junit.Test;

/**
 * Given an array of integers, return indices of the two numbers such that they
 * add up to a specific target. You may assume that each input would have
 * exactly one solution, and you may not use the same element twice. Example:
 * Given nums = [2, 7, 11, 15], target = 9,
 * 
 * Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
 * 
 * 
 * 
 * Due: 11/10/2018 23:59 UTC
 * 
 * Submission Requirements:
 * 
 * 1. Please create your own branch and push your work on your own branch. 2.
 * The file name should include your nickname
 * 
 * 
 * Sample: TwoSumDavidWu.java two_sum_david_wu.py
 * 
 * 3. Please add code to the folder associated with your programming language.
 * 
 * (i.e. If you use Java, please add your java file under java folder. )
 *
 */
public class TwoSum {

	@Test
	public void test_TwoSum() {
		int[] nums = { 2, 7, 11, 15 };
		int target = 9;
		int[] expect = { 0, 1 };
		Assert.assertArrayEquals(getTwoSum(nums, target), expect);
		Assert.assertArrayEquals(twoSum(nums, target), expect);
	}

	private int[] getTwoSum(int[] nums, int target) {
		int[] result = new int[2];
		Map<Integer, Integer> tmp = new HashMap<>();
		for (int i = 0; i < nums.length; i++) {
			tmp.put(nums[i], i);
		}

		for (int i = 0; i < nums.length; i++) {
			if (tmp.containsKey(target - nums[i])) {
				result[0] = i;
				result[1] = tmp.get(target - nums[i]);
//				in case of 4 = 2 + 2, but there is only one 2 element
				if(i != tmp.get(target - nums[i])) {
					return result;
				}
			}
		}
		return result;
	}
	
	private int[] twoSum(int[] nums, int target) {
		Map<Integer, Integer> map = new HashMap<>();
		for(int i = 0; i < nums.length; i++) {
			if(map.containsKey(nums[i])) {
//				nums[i] is the second element
				return new int[] {map.get(nums[i]), i};
			} else {
//				key:second element; value: the index of first element
				map.put(target - nums[i], i);
			}
		}
		return new int[] {0, 0};
	}
}
