# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next
        
        stack.pop(len(stack) - n)
        if not stack:
            return None

        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        stack[-1].next = None

        return stack[0]