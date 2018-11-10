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
        ListNode res = new ListNode(0);
        if(l1 == null && l2 == null) return res;
        if(l1 == null || l2 == null) return l1 == null ? l2:l1;
        int over = 0;
        ListNode dummy = new ListNode(0);
        dummy.next = res;
        while(l1 != null || l2 != null || over != 0) {
            int temp = 0;
            res.next = new ListNode(0);
            res = res.next;
            if(l1 != null) {
                temp += l1.val;
                l1 = l1.next;
            }
            if(l2 != null) {
                temp += l2.val;
                l2 = l2.next;
            }
            temp+=over;
            res.val = temp%10;
            over = temp/10;
        }
        return dummy.next.next;
        
    }
}
