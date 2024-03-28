from solution2 import Solution

s2 = Solution()

# case 1
print("Case 1")
print("Input: s = 'A man, a plan, a canal: Panama'")
s = 'A man, a plan, a canal: Panama'
print("Output: ", s2.isPalindrome(s))
print("Expected: true")

# case 2
print("Case 2")
print("Input: s = 'race a car'")
s = 'race a car'
print("Output: ", s2.isPalindrome(s))
print("Expected: False")

# case 2
print("Case 2")
print("Input: s = ' '")
s = ' '
print("Output: ", s2.isPalindrome(s))
print("Expected: True")
