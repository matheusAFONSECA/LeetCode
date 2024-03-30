from solution3 import Solution

s2 = Solution()

# case 1
print("Case 1")
print("Input: s = 'aba'")
s = 'aba'
print("Output: ", s2.validPalindrome(s))
print("Expected: True")

# case 2
print("Case 2")
print("Input: s = 'abca'")
s = 'abca'
print("Output: ", s2.validPalindrome(s))
print("Expected: True")

# case 3
print("Case 3")
print("Input: s = 'abc'")
s = 'abc'
print("Output: ", s2.validPalindrome(s))
print("Expected: False")

# case 4
print("Case 4")
print("Input: s = 'pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip'")
s = 'pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip'
print("Output: ", s2.validPalindrome(s))
print("Expected: False")
