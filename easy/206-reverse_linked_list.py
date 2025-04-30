class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            # Reverse direction of current node
            nxt = curr.next       
            curr.next = prev      

            # Shift to next node
            prev = curr           
            curr = nxt            

        return prev   
