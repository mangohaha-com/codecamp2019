package java;

import org.junit.Assert;
import org.junit.Test;

/**
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21


Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
 * @author xx65
 *
 */
public class ReverseInteger_7 {
	
	@Test
	public void test_ReverseInteger() {
		int a = 123;
		int b = -897;
		Assert.assertEquals(321, reverseInteger(a));
		Assert.assertEquals(-798, reverseInteger(b));
	}

	/**
	 * input integer range: [−2^31,  2^31 − 1]  -> [-2147483648, 2147483647]
	 * if input = 2140000009, we could not get 9000000412, it's out of range
	 */
	private static int reverseInteger(int num) {
		int res = 0;
		while( num != 0) {
			int pop = num % 10;
			num /= 10;
			if(res > Integer.MAX_VALUE / 10 || res < Integer.MIN_VALUE) {
				return 0;
			}
			res = res * 10 + pop;
		}
		return res;
	}
}
