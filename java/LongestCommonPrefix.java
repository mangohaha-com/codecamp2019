package java;

import org.junit.Assert;
import org.junit.Test;

/**
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
 *
 */
public class LongestCommonPrefix {

	@Test
	public void test_LongestCommonPrefix() {
		String[] input = {"flower","flow","flight"};
		Assert.assertEquals("fl", getLongestCommonPrefix(input));
	}
	
	private static String getLongestCommonPrefix(String[] strs) {
		if(strs == null || strs.length < 1) {
			return "";
		}
		String minStr = strs[0];
        for(int i = 1; i < strs.length; i++) {
            minStr = minStr.length() > strs[i].length() ? strs[i] : minStr;
        }

        if(minStr == null || minStr.length() < 1) {
        	return "";
        }
        
        for(int i = 0; i < strs.length; i++) {
           String ans = findCommonPrefix(minStr, strs[i]);
           minStr = ans;
        }
        return minStr;
    }
    
    private static String findCommonPrefix(String minStr, String tmp) {
        int count = -1;
        for(int i = 0; i < minStr.length(); i++) {
            if(minStr.charAt(i) == tmp.charAt(i)) {
                count = i;
            } else {
                break;
            }
        }
        if(count == -1) {
        	return "";
        } else {
        	return new String(minStr).substring(0, count + 1);
        }
    }
}
