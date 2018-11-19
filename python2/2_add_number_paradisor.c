/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* ret = malloc(sizeof(struct ListNode));
    struct ListNode* l3 = ret;
    ret->val = ret->next = NULL;
    int carry = 0;
    while(l1 != NULL || l2 != NULL) {
        int v1 = l1 ? l1->val : 0;
        int v2 = l2 ? l2->val : 0;
        int v3 = v1 + v2 + carry;
        l3->val = v3 % 10;
        carry = v3 / 10;
        l1 = l1 ? l1->next : NULL;
        l2 = l2 ? l2->next : NULL;
        if (l1 == NULL && l2 == NULL && carry == 0) {
            return ret;
        }
        l3->next = malloc(sizeof(struct ListNode));
        l3->next->val = 1;
        l3->next->next = NULL;
        l3 = l3->next;
    }
    return ret;
}