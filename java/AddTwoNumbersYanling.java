/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class AddTwoNumbersYanling {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        //carry value
        int flag = 0;
        //dummy head
        ListNode dummy = new ListNode(0);
        ListNode result = dummy;
        while (l1 != null && l2 != null){
            int value = (flag + l1.val + l2.val)%10;
            flag = (flag + l1.val + l2.val)/10;
            result.next = new ListNode(value);
            result = result.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        
        while (l1 != null){
            int value = (flag + l1.val)%10;
            flag = (flag + l1.val)/10;
            result.next = new ListNode(value);
            result = result.next;
            l1 = l1.next;
        }
        
        while (l2 != null){
            int value = (flag + l2.val)%10;
            flag = (flag + l2.val)/10;
            result.next = new ListNode(value);
            result = result.next;
            l2 = l2.next;
        }
        
        //MSB
        if (flag > 0 ){
            result.next = new ListNode(flag);
        }
        return dummy.next;
    }
    
    
}

//Go through two linked lists from heads to tails
//Time Complexity: O(n)
//Space Complexity: O(n)