from solution1 import Solution, ListNode

# Function to convert a Python list to a linked list
def list_to_linked_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

s = Solution()

# case 1
print("Case 1")
print("head = [1,2,2,1]")
head1 = list_to_linked_list([1,2,2,1])
print("Output: ", s.isPalindrome(head1))
print("Expected: True")

# case 2
print("Case 2")
print("head = [1,2]")
head2 = list_to_linked_list([1,2])
print("Output: ", s.isPalindrome(head2))
print("Expected: False")
