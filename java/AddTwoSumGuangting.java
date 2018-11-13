/**
 * Definition for singly-linked list. public class ListNode { int val; ListNode next; ListNode(int
 * x) { val = x; } }
 */
class AddTwoSumGuangting {

  public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummyNode = new ListNode(0);
    ListNode p = dummyNode;
    ListNode p1 = l1;
    ListNode p2 = l2;

    int carrier = 0;
    while (p1 != null || p2 != null) {
      int val = 0;
      if (p1 == null) {
        val = carrier + p2.val;
        carrier = val / 10;
        val %= 10;
        ListNode next = new ListNode(val);
        p.next = next;
        p = p.next;
        p2 = p2.next;
        continue;
      }

      if (p2 == null) {
        val = carrier + p1.val;
        carrier = val / 10;
        val %= 10;
        ListNode next = new ListNode(val);
        p.next = next;
        p = p.next;
        p1 = p1.next;
        continue;
      }

      val = p1.val + p2.val + carrier;
      carrier = val / 10;
      val %= 10;
      ListNode next = new ListNode(val);
      p.next = next;
      p = p.next;
      p1 = p1.next;
      p2 = p2.next;
    }
    if (carrier != 0) {
      ListNode next = new ListNode(carrier);
      p.next = next;
    }
    return dummyNode.next;
  }
}