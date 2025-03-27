# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        stack = []

        while curr != None:
            stack.append(curr)
            curr = curr.next

        new_head = stack.pop()
        curr_node = new_head
        
        while stack:
            curr_node.next = stack.pop()
            curr_node = curr_node.next

        curr_node.next = None

        return new_head
