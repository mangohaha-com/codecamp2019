/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class RemoveDupFromSortedListYanling {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null)
            return head;
        ListNode curr = head;
        while(curr.next!=null && curr.next.next!= null){
            if(curr.val == curr.next.val){
                curr.next = curr.next.next;
                //curr->curr.next
                //curr->curr.next.next
                //curr stay unchange to handle more than two duplicates cases
            }
            else
                curr = curr.next;
        }
        //handle dup at tail cases
        if(curr.next!=null && curr.val == curr.next.val)
            curr.next = null;
        return head;
    }
}

//Time Complexity: O(n)
//Spacer Complexity:O(1)