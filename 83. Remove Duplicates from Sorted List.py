# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        l=list(set(l))
        l.sort()
        a=ListNode(0)
        temp=a
        for i in l:
            temp.next=ListNode(i)
            temp=temp.next
        return a.next
