class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        lst.reverse()
        l=[]
        for i in range(len(lst)):
            if i!=n-1:
                l.append(lst[i])
        l.reverse()
        a=ListNode(0)
        temp=a
        for i in l:
            temp.next=ListNode(i)
            temp=temp.next
        return a.next
