class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l=[]
        for i in lists:
            while i:
                l.append(i.val)
                i=i.next
        l.sort()
        a=ListNode(0)
        temp=a
        for i in l:
            temp.next=ListNode(i)
            temp=temp.next
        return a.next
