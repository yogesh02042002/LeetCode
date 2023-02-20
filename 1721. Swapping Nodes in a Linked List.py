class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        l[k-1],l[-k]=l[-k],l[k-1]
        a=ListNode(0)
        temp=a
        for i in l:
            temp.next=ListNode(i)
            temp=temp.next
        return a.next
