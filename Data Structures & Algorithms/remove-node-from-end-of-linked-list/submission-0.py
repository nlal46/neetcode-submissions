# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        ####
        s = head
        i = 1
        while (s is not None):
            s = s.next
            i = i + 1 #i now gives total nodes + 1

        y = i - n  #node to delete from the start

        if y == 1:
            head = head.next
            return head
        else:
            q = head
            p = head.next
            i = 1
            while (i < y - 1):
                p = p.next
                q = q.next
                i = i + 1
            q.next = p.next
            p.next = q.next
            return head






        
