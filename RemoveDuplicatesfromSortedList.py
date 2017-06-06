# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


def python_list(ListNode):
    pl = []
    while ListNode is not None:
        pl.append(ListNode.val)
        ListNode = ListNode.next
    return pl


def linked_list(py_list):
    if len(py_list) == 0:
        return None
    else:
        head = ListNode(py_list[0])
        p = head
        for i in range(1, len(py_list)):
            head.next = ListNode(py_list[i])
            head = head.next
        return p


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        ls = python_list(head)
        i = 0
        while i < len(ls)-1:
            if ls[i] == ls[i+1]:
                ls.pop(i)
            else:
                i += 1
        return linked_list(ls)

