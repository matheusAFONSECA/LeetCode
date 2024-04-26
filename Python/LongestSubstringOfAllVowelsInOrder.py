class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:

        return 2

def main():         # função principal
    s = Solution()      # instanciando o objeto

    # case 1
    print("Case 1")
    print("Input: word = 'aeiaaioaaaaeiiiiouuuooaauuaeiu'")
    n = 'aeiaaioaaaaeiiiiouuuooaauuaeiu'
    print("Output: ", s.longestBeautifulSubstring(n))
    print("Expected: 13")

    # case 2
    print("Case 2")
    print("Input: word = 'aeeeiiiioooauuuaeiou'")
    n = 'aeeeiiiioooauuuaeiou'
    print("Output: ", s.longestBeautifulSubstring(n))
    print("Expected: 5")

    # case 3
    print("Case 3")
    print("Input: word = 'a'")
    n = 'a'
    print("Output: ", s.longestBeautifulSubstring(n))
    print("Expected: 0")

if __name__ == "__main__":
    main()
