from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Função para reverter uma lista ligada
        def reverseList(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev
        
        # Função para achar o meio de uma lista ligada
        def findMiddle(node):
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        # Revertendo a metade da lista
        middle = findMiddle(head)
        second_half = reverseList(middle)
        
        # Compara os valores da primeira e segunda metade
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        return True
