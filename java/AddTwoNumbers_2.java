package java;

import org.junit.Test;

/**
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
 */
public class AddTwoNumbers_2 {

	@Test
	public void test_AddTwoNumbers() {
//		2->4->3
		ListNode input1 = new ListNode(2);
		ListNode input2 = new ListNode(4);
		ListNode input3 = new ListNode(3);
		input1.next = input2;
		input2.next = input3;
//		9
		ListNode input4 = new ListNode(9);
		System.out.println(addTwoNumbers( input1, input4));
	}
	
	private ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		int carry = 0;
		ListNode dumyHead = new ListNode(0);
		ListNode head = dumyHead;
		while(l1 != null || l2 != null) {
			int v1 = l1 != null ? l1.value : 0;
			int v2 = l2 != null ? l2.value : 0;
			int sum = carry + v1 + v2;
			dumyHead.next = new ListNode(sum % 10);
			carry = sum / 10;
			dumyHead = dumyHead.next;
			l1 = l1 != null ? l1.next : l1;
			l2 = l2 != null ? l2.next : l2;
		}
		if(carry > 0) {
			dumyHead.next = new ListNode(carry);
		}
		return head.next;
	}
}
