class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        count = 0           # contador para quando as condições são satisfeitas

        return count
    

def main():         # função principal

    s = Solution()      # instanciando o objeto

    # case 1
    print("Case 1")
    print("Input: s = 'abcabcbb'")
    n = "abcabcbb"
    print("Output: ", s.lengthOfLongestSubstring(n))
    print("Expected: 3")

    # case 2
    print("Case 2")
    print("Input: s = 'bbbbb'")
    n = "bbbbb"
    print("Output: ", s.lengthOfLongestSubstring(n))
    print("Expected: 1")

    # case 3
    print("Case 3")
    print("Input: s = 'pwwkew'")
    n = "pwwkew"
    print("Output: ", s.lengthOfLongestSubstring(n))
    print("Expected: 3")


if __name__ == "__main__":
    main()
    