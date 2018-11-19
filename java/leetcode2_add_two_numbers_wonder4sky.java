/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode start = new ListNode(0);
        ListNode head = start;
        int carry = 0;

        // carry != 0也是循环的一个条件之一，否则8+2的情况则无法处理
        while (l1 != null || l2 != null || carry != 0) {
            int total = (l1 == null?0:l1.val) + (l2 == null?0:l2.val) + carry;
            //l1 = (l1 ? l1.next: 0);
            //l2 = (l2 ? l2.next: 0);
            carry = total / 10;
            start.next = new ListNode(total % 10);
            start = start.next;

            if (l1 != null)
                l1 = l1.next;

            if (l2 != null)
                l2 = l2.next;

        }
        return head.next;
    }
}