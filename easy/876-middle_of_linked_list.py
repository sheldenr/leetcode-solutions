# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length, index = 0, 0
        curr_node = head

        if not head.next:
            return head

        # Determine length of linked lsit
        while curr_node:
            length += 1
            curr_node = curr_node.next

        curr_node = head
        curr_index = 0
        
        if length % 2 == 0:
            middle_index = ((length + 1) // 2)
        else:
            middle_index = ((length + 1) // 2) - 1

        while curr_node:
            curr_index += 1
            curr_node = curr_node.next

            if curr_index == middle_index:
                return curr_node

            

