"""
week two
"""

import random

class ListNode():
    """
    one node for a list
    include value and next node
    """

    def __init__(self, x):
        self.val = x
        self.next = None

class AddTwoNumber():
    """
    add two numbers
    """

    @staticmethod
    def get_dig(nb_a, nb_b):
        """
        find single digit
        if it over 10, the flag will be set to 1
        """
        flag = 0
        tmp = nb_a + nb_b
        if tmp >= 10:
            result = tmp - 10
            flag = 1
        else:
            result = tmp

        return result, flag

    def add_two_number(self, nd_a, nd_b):
        """
        function for add two numbers
        """
        flag = 0
        rst_tmp = ListNode(0)
        result = rst_tmp

        while not nd_a.next is None:
            if flag == 1:
                nd_a.val += 1
            rst_tmp.val, flag_tmp = AddTwoNumber.get_dig(nd_a.val, nd_b.val)
            flag = flag_tmp

            nd_a = nd_a.next
            nd_b = nd_b.next
            rst_tmp.next = ListNode(0)
            rst_tmp = rst_tmp.next

        if flag == 1:
            nd_a.val += 1
        rst_tmp.val, flag_tmp = AddTwoNumber.get_dig(nd_a.val, nd_b.val)
        if flag_tmp == 1:
            rst_tmp.next = ListNode(1)

        return result

if __name__ == '__main__':
    i = 0
    NT_A = ListNode(random.randint(0, 9))
    NT_B = ListNode(random.randint(0, 9))
    TMP_A = NT_A
    TMP_B = NT_B
    NODE_A = TMP_A
    NODE_B = TMP_B
    while i < 2:
        print("create nodes at {0}".format(i))
        NT_A.next = ListNode(random.randint(0, 9))
        NT_B.next = ListNode(random.randint(0, 9))
        NT_A = NT_A.next
        NT_B = NT_B.next
        i += 1

    i = 0
    while i < 3:
        print("a{0} -> {1} ".format(i, NODE_A.val), end="")
        NODE_A = NODE_A.next
        i += 1
    print()

    i = 0
    while i < 3:
        print("b{0} -> {1} ".format(i, NODE_B.val), end="")
        NODE_B = NODE_B.next
        i += 1
    print()

    NODE_A = TMP_A
    NODE_B = TMP_B
    ADT = AddTwoNumber()
    RST = ADT.add_two_number(NODE_A, NODE_B)
    MY_RST = RST


    i = 0
    while not MY_RST.next is None:
        print("node{0} -> {1} ".format(i, MY_RST.val), end="")
        MY_RST = MY_RST.next
        i += 1

    print("node{0} -> {1}".format(i, MY_RST.val))
