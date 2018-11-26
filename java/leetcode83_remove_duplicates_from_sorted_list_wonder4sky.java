public class leetcode83_remove_duplicates_from_sorted_list_wonder4sky {

    /**
     * Definition for singly-linked list.
     * public class ListNode {
     * int val;
     * ListNode next;
     * ListNode(int x) { val = x; }
     * }
     */
    class Solution {
        public ListNode deleteDuplicates(ListNode head) {
            // 感觉和实现strStr()那道题很像，都是分成三部分的思路
            if (head == null || head.next == null)
                return head;

            ListNode first = head;
            ListNode second = first;

            //注意是second != null,  而不是second.next != null 因为后面用到的是second.next, 而不是second.next.next
            while (second != null) {

                //这一段的思路与＃28 strStr()的思路很像：三段式，两个指针
                if (second.val != first.val) {
                    first.next = second;
                    first = second;
                    second = second.next;
                } else {
                    second = second.next;

                    // 考虑corner case：就是second走到了最后一个时，应该把first.next 指向null
                    if (second == null) {
                        first.next = null;
                    }
                }
            }
            return head;
        }
    }
}

