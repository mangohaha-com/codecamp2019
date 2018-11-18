public class Solution {
    public ListNode addTwoNumbersDW(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int sum = carry;
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
            carry = sum/10;
            sum = sum%10;
            ListNode node = new ListNode(sum);
            cur.next = node;
            cur = cur.next;
        }
        return dummy.next;
    }
}
