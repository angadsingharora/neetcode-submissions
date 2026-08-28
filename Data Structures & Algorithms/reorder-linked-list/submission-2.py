# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #iterate through whole list store as stack. top of stack will be last element. so like alternating head pointer and popping off stack until some some happens
        stack = []
        curr = head
   

        while curr:
            stack.append(curr)
            curr = curr.next
        curr = head

        for i in range(len(stack)//2):
            last = stack.pop()
            nextNode = curr.next

            curr.next = last
            last.next = nextNode

            curr = nextNode

        curr.next = None
        
            
