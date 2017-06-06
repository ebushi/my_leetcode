# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode(object):
    
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return str(self.val)
        

def Linkedlist(pythonlist):
    l = ListNode(pythonlist[0])
    c = l
    for i in range(1, len(pythonlist)):
        l.next = ListNode(pythonlist[i])
        l = l.next
    return c
    

def Pythonlist(ListNode):
    l = []
    while ListNode != None:
        l.append(ListNode.val)
        ListNode = ListNode.next
    return l
    

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        dummyhead = ListNode(0)
        dummyhead.next = None
        p = dummyhead
        
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
            
            if l1 is not None:
                p.next = l1
            else:
                p.next = l2
        return dummyhead.next
