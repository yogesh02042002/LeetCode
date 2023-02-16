class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        l=[]
        while head:
            if head.val==val:
                head=head.next
            else:
                l.append(head.val)
                head=head.next
        a=ListNode(0)
        temp=a
        for i in l:
            temp.next=ListNode(i)
            temp=temp.next
        return a.next
